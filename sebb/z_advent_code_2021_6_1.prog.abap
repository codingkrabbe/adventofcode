REPORT z_advent_code_2021_6_1.

DATA:
  depth        TYPE i,
  horizontal   TYPE i,
  input_lines  TYPE TABLE OF string,
  fish         TYPE TABLE OF string,
  new_fish     TYPE TABLE OF string,
  initial_fish TYPE string VALUE '8'.

cl_gui_frontend_services=>gui_upload( EXPORTING filename = 'C:\Data\AdventOfCode\Day6input.txt'
                                      CHANGING  data_tab = input_lines ).
SPLIT input_lines[ 1 ] AT ',' INTO TABLE fish.
DO 256 TIMES.
  LOOP AT fish ASSIGNING FIELD-SYMBOL(<current_fish>).
    IF CONV i( <current_fish> ) = '0'.
      <current_fish> = '6'.
      APPEND initial_fish TO new_fish.
    ELSE.
      <current_fish> = <current_fish> - 1.
    ENDIF.
  ENDLOOP.
  APPEND LINES OF new_fish TO fish.
  CLEAR new_fish.
ENDDO.

WRITE: |{ lines( fish ) }|.
