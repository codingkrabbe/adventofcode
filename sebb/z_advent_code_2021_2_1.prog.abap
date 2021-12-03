REPORT z_advent_code_2021_2_1.

DATA:
  depth             TYPE i,
  horizontal        TYPE i,
  input_lines       TYPE TABLE OF string.

cl_gui_frontend_services=>gui_upload( EXPORTING filename = 'C:\Data\AdventOfCode\Day2input.txt'
                                      CHANGING  data_tab = input_lines ).

LOOP AT input_lines INTO DATA(input_line).
  SPLIT input_line AT space INTO: DATA(command) DATA(value).
  CASE command.
    WHEN 'forward'. horizontal = horizontal + value.
    WHEN 'down'. depth = depth + value.
    WHEN 'up'. depth = depth - value.
  ENDCASE.
ENDLOOP.

WRITE: |{ depth * horizontal }|.
