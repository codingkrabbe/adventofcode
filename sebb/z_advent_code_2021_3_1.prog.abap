REPORT z_advent_code_2021_3_1.
TYPES: BEGIN OF ty_split,
         pos1  TYPE i,
         pos2  TYPE i,
         pos3  TYPE i,
         pos4  TYPE i,
         pos5  TYPE i,
         pos6  TYPE i,
         pos7  TYPE i,
         pos8  TYPE i,
         pos9  TYPE i,
         pos10 TYPE i,
         pos11 TYPE i,
         pos12 TYPE i,
       END OF ty_split.
DATA:
  input_lines TYPE TABLE OF string,
  split_line  TYPE ty_split,
  sum         TYPE ty_split,
  gamma       TYPE ty_split,
  epsilon     TYPE ty_split,
  split_table TYPE TABLE OF ty_split.

cl_gui_frontend_services=>gui_upload( EXPORTING filename = 'C:\Data\AdventOfCode\Day3input.txt'
                                      CHANGING  data_tab = input_lines ).

LOOP AT input_lines INTO DATA(input_line).
  split_line-pos1 = input_line+0(1).
  split_line-pos2 = input_line+1(1).
  split_line-pos3 = input_line+2(1).
  split_line-pos4 = input_line+3(1).
  split_line-pos5 = input_line+4(1).
  split_line-pos6 = input_line+5(1).
  split_line-pos7 = input_line+6(1).
  split_line-pos8 = input_line+7(1).
  split_line-pos9 = input_line+8(1).
  split_line-pos10 = input_line+9(1).
  split_line-pos11 = input_line+10(1).
  split_line-pos12 = input_line+11(1).
  APPEND split_line TO split_table.
ENDLOOP.
LOOP AT split_table INTO DATA(line).
  AT LAST. SUM. sum = line. ENDAT.
ENDLOOP.
gamma = VALUE #(    pos1 = round( val = sum-pos1 / lines( input_lines ) dec = 0 )
                    pos2 = round( val = sum-pos2 / lines( input_lines ) dec = 0 )
                    pos3 = round( val = sum-pos3 / lines( input_lines ) dec = 0 )
                    pos4 = round( val = sum-pos4 / lines( input_lines ) dec = 0 )
                    pos5 = round( val = sum-pos5 / lines( input_lines ) dec = 0 )
                    pos6 = round( val = sum-pos6 / lines( input_lines ) dec = 0 )
                    pos7 = round( val = sum-pos7 / lines( input_lines ) dec = 0 )
                    pos8 = round( val = sum-pos8 / lines( input_lines ) dec = 0 )
                    pos9 = round( val = sum-pos9 / lines( input_lines ) dec = 0 )
                    pos10 = round( val = sum-pos10 / lines( input_lines ) dec = 0 )
                    pos11 = round( val = sum-pos11 / lines( input_lines ) dec = 0 )
                    pos12 = round( val = sum-pos12 / lines( input_lines ) dec = 0 ) ).
epsilon = VALUE #(  pos1 = SWITCH i( gamma-pos1 WHEN 0 THEN 1 ELSE 0 )
                    pos2 = SWITCH i( gamma-pos2 WHEN 0 THEN 1 ELSE 0 )
                    pos3 = SWITCH i( gamma-pos3 WHEN 0 THEN 1 ELSE 0 )
                    pos4 = SWITCH i( gamma-pos4 WHEN 0 THEN 1 ELSE 0 )
                    pos5 = SWITCH i( gamma-pos5 WHEN 0 THEN 1 ELSE 0 )
                    pos6 = SWITCH i( gamma-pos6 WHEN 0 THEN 1 ELSE 0 )
                    pos7 = SWITCH i( gamma-pos7 WHEN 0 THEN 1 ELSE 0 )
                    pos8 = SWITCH i( gamma-pos8 WHEN 0 THEN 1 ELSE 0 )
                    pos9 = SWITCH i( gamma-pos9 WHEN 0 THEN 1 ELSE 0 )
                    pos10 = SWITCH i( gamma-pos10 WHEN 0 THEN 1 ELSE 0 )
                    pos11 = SWITCH i( gamma-pos11 WHEN 0 THEN 1 ELSE 0 )
                    pos12 = SWITCH i( gamma-pos12 WHEN 0 THEN 1 ELSE 0 ) ).

DATA(gamma_value) = /ui2/cl_number=>base_converter(
    number = |{ gamma-pos1 }{ gamma-pos2 }{ gamma-pos3 }{ gamma-pos4 }{ gamma-pos5 }{ gamma-pos6 }{ gamma-pos7 }{ gamma-pos8 }{ gamma-pos9 }{ gamma-pos10 }{ gamma-pos11 }{ gamma-pos12 }|
    from = 2 to = 10 ).
DATA(epsilon_value) = /ui2/cl_number=>base_converter(
    number = |{ epsilon-pos1 }{ epsilon-pos2 }{ epsilon-pos3 }{ epsilon-pos4 }{ epsilon-pos5 }{ epsilon-pos6 }{ epsilon-pos7 }{ epsilon-pos8 }{ epsilon-pos9 }{ epsilon-pos10 }{ epsilon-pos11 }{ epsilon-pos12 }|
    from = 2 to = 10 ).

WRITE CONV string( gamma_value * epsilon_value ).
