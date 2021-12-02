REPORT z_advent_code_2021_1_1.

  DATA:
    input_lines       TYPE TABLE OF i,
    increased_counter TYPE i VALUE 0,
    last_line         LIKE LINE OF input_lines.

  cl_gui_frontend_services=>gui_upload( EXPORTING filename = 'C:\Data\AdventOfCode\Day1input.txt'
                                        CHANGING  data_tab = input_lines ).

  LOOP AT input_lines INTO DATA(input_line).
    IF last_line > 0 AND input_line > last_line.
      increased_counter = increased_counter + 1.
    ENDIF.
    last_line = input_line.
  ENDLOOP.

  WRITE: increased_counter.
