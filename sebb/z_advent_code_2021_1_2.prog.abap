REPORT z_advent_code_2021_1_2.

DATA:
  input_lines        TYPE TABLE OF i,
  current_window_sum TYPE i,
  last_window_sum    TYPE i,
  increased_counter  TYPE i VALUE 0.

  cl_gui_frontend_services=>gui_upload( EXPORTING filename = 'C:\Data\AdventOfCode\Day1input.txt'
                                        CHANGING  data_tab = input_lines ).

LOOP AT input_lines INTO DATA(input_line).
  IF sy-tabix > 2.
    current_window_sum = input_line + input_lines[ sy-tabix - 1 ] + input_lines[ sy-tabix - 2 ].
    IF last_window_sum > 0 AND current_window_sum > last_window_sum.
      increased_counter = increased_counter + 1.
    ENDIF.
    last_window_sum = current_window_sum.
  ENDIF.
ENDLOOP.

WRITE: increased_counter.
