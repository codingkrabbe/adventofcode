REPORT z_advent_code_2021_2_2.

DATA:
  depth             TYPE i,
  horizontal        TYPE i,
  aim TYPE i,
  input_lines       TYPE TABLE OF string.

cl_gui_frontend_services=>gui_upload( EXPORTING filename = 'C:\Data\AdventOfCode\Day2input.txt'
                                      CHANGING  data_tab = input_lines ).

LOOP AT input_lines INTO DATA(input_line).
  SPLIT input_line AT space INTO: DATA(command) DATA(value).
  CASE command.
    WHEN 'forward'. horizontal = horizontal + value.
                    depth      = depth + ( aim * value ).
    WHEN 'down'. aim = aim + value.
    WHEN 'up'. aim = aim - value.
  ENDCASE.
ENDLOOP.

WRITE: |{ depth * horizontal }|.
