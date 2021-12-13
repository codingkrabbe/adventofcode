REPORT z_advent_code_2021_11_1.

CLASS cx_octo_error DEFINITION INHERITING FROM cx_static_check.ENDCLASS.
CLASS octopus DEFINITION.
  PUBLIC SECTION.
    METHODS:
      constructor
        IMPORTING
          i_x    TYPE i
          i_y    TYPE i
          energy TYPE i,

      get_x RETURNING VALUE(r_result) TYPE i,
      get_y RETURNING VALUE(r_result) TYPE i,
      flash,
      reset_flashed,
      add_energy.
  PRIVATE SECTION.
    DATA:
      x       TYPE i,
      y       TYPE i,
      flashed TYPE boole_d,
      energy  TYPE i.
ENDCLASS.

CLASS octopus_collection DEFINITION.
  PUBLIC SECTION.
    CLASS-METHODS:
      add      IMPORTING i_x    TYPE i
                         i_y    TYPE i
                         energy TYPE i,
      get_by_coord      IMPORTING i_x         TYPE i
                                  i_y         TYPE i
                        RETURNING VALUE(octo) TYPE REF TO octopus
                        RAISING   cx_octo_error,
      increase_flashed_counter,
      execute_step.
    CLASS-METHODS: get_flashed_counter RETURNING VALUE(r_result) TYPE i.
  PRIVATE SECTION.
    CLASS-DATA:
      flashed_counter TYPE i,
      octopuses       TYPE TABLE OF REF TO octopus.
ENDCLASS.

TYPES: BEGIN OF penalties_line,
         char    TYPE c,
         penalty TYPE i,
       END OF penalties_line,

       BEGIN OF chunk_pair,
         opener TYPE c,
         closer TYPE c,
       END OF chunk_pair.
DATA:
  input_lines TYPE TABLE OF string,
  y           TYPE i,
  x           TYPE i.

cl_gui_frontend_services=>gui_upload( EXPORTING filename = 'C:\Data\AdventOfCode\Day11input.txt'
                                      CHANGING  data_tab = input_lines ).

LOOP AT input_lines INTO DATA(input_line).
  y = sy-tabix.
  DO strlen( input_line ) TIMES.
    x = sy-index.
    DATA(offset) = x - 1.
    DATA(current_input_char) = input_line+offset(1) .
    octopus_collection=>add( i_x = x
                             i_y = y
                             energy = CONV #( current_input_char ) ).
  ENDDO.
ENDLOOP.
DO 100 TIMES.
  octopus_collection=>execute_step( ).
  WRITE: |Flashes after round { sy-index }: { octopus_collection=>get_flashed_counter( ) }|.
  NEW-LINE.
ENDDO.
WRITE: |{ octopus_collection=>get_flashed_counter( ) }|.

CLASS octopus_collection IMPLEMENTATION.

  METHOD get_by_coord.
    LOOP AT octopuses ASSIGNING FIELD-SYMBOL(<octo>).
      IF <octo>->get_x( ) = i_x AND <octo>->get_y( ) = i_y.
        octo = <octo>.
        RETURN.
      ENDIF.
    ENDLOOP.
    RAISE EXCEPTION TYPE cx_octo_error.
  ENDMETHOD.

  METHOD add.
    DATA(new_octo) = NEW octopus( i_x = i_x i_y = i_y energy = energy ).
    APPEND new_octo TO octopuses.
  ENDMETHOD.


  METHOD execute_step.
    FIELD-SYMBOLS: <current_octo> TYPE REF TO octopus.
    LOOP AT octopuses ASSIGNING <current_octo>.
      <current_octo>->add_energy( ).
    ENDLOOP.
    LOOP AT octopuses ASSIGNING <current_octo>.
      <current_octo>->reset_flashed( ).
    ENDLOOP.
  ENDMETHOD.

  METHOD increase_flashed_counter.
    flashed_counter = flashed_counter + 1.
  ENDMETHOD.

  METHOD get_flashed_counter.
    r_result = flashed_counter.
  ENDMETHOD.

ENDCLASS.

CLASS octopus IMPLEMENTATION.

  METHOD constructor.
    me->x = i_x.
    me->y = i_y.
    me->energy = energy.
    flashed = abap_false.
  ENDMETHOD.

  METHOD flash.
    DATA: adjacent_octo TYPE REF TO octopus.
    IF flashed = abap_true .
      RETURN.
    ENDIF.
    flashed = abap_true.
    octopus_collection=>increase_flashed_counter( ).
    energy = 0.

    DATA(adjacent_y1) = y - 1.
    DATA(adjacent_y2) = y + 1.
    DATA(adjacent_x1) = x - 1.
    DATA(adjacent_x2) = x + 1.
    TRY.
        adjacent_octo = octopus_collection=>get_by_coord(
            i_x = adjacent_x1
            i_y = adjacent_y1 ).
        adjacent_octo->add_energy( ).
      CATCH cx_octo_error.
    ENDTRY.
    TRY.
        adjacent_octo = octopus_collection=>get_by_coord(
            i_x = x
            i_y = adjacent_y1 ).
        adjacent_octo->add_energy( ).
      CATCH cx_octo_error.
    ENDTRY.
    TRY.
        adjacent_octo = octopus_collection=>get_by_coord(
            i_x = adjacent_x2
            i_y = adjacent_y1 ).
        adjacent_octo->add_energy( ).
      CATCH cx_octo_error.
    ENDTRY.
    TRY.
        adjacent_octo = octopus_collection=>get_by_coord(
            i_x = adjacent_x1
            i_y = y ).
        adjacent_octo->add_energy( ).
      CATCH cx_octo_error.
    ENDTRY.
    TRY.
        adjacent_octo = octopus_collection=>get_by_coord(
            i_x = adjacent_x2
            i_y = y ).
        adjacent_octo->add_energy( ).
      CATCH cx_octo_error.
    ENDTRY.
    TRY.
        adjacent_octo = octopus_collection=>get_by_coord(
            i_x = adjacent_x1
            i_y = adjacent_y2 ).
        adjacent_octo->add_energy( ).
      CATCH cx_octo_error.
    ENDTRY.
    TRY.
        adjacent_octo = octopus_collection=>get_by_coord(
            i_x = x
            i_y = adjacent_y2 ).
        adjacent_octo->add_energy( ).
      CATCH cx_octo_error.
    ENDTRY.
    TRY.
        adjacent_octo = octopus_collection=>get_by_coord(
            i_x = adjacent_x2
            i_y = adjacent_y2 ).
        adjacent_octo->add_energy( ).
      CATCH cx_octo_error.
    ENDTRY.
  ENDMETHOD.

  METHOD get_x.
    r_result = me->x.
  ENDMETHOD.

  METHOD get_y.
    r_result = me->y.
  ENDMETHOD.

  METHOD add_energy.
    IF flashed = abap_true.
      RETURN.
    ENDIF.
    energy = energy + 1.
    IF energy > 9.
      flash( ).
    ENDIF.
  ENDMETHOD.

  METHOD reset_flashed.
    flashed = abap_false.
  ENDMETHOD.

ENDCLASS.
