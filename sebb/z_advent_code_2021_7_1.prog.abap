REPORT z_advent_code_2021_7_1.

DATA:
  input_lines  TYPE TABLE OF string,
  string_crabs TYPE TABLE OF string,
  number_crabs TYPE TABLE OF sls_nums,
  number_crab  TYPE sls_nums,
  median       TYPE ls_median,
  fuel         TYPE i.

cl_gui_frontend_services=>gui_upload( EXPORTING filename = 'C:\Data\AdventOfCode\Day7input.txt'
                                      CHANGING  data_tab = input_lines ).
SPLIT input_lines[ 1 ] AT ',' INTO TABLE string_crabs.
LOOP AT string_crabs ASSIGNING FIELD-SYMBOL(<string_crab>).
  number_crab-number = 0 + <string_crab>.
  APPEND number_crab TO number_crabs.
ENDLOOP.
CALL FUNCTION 'SLS_MISC_GET_MEDIAN'
  IMPORTING
    median = median
  TABLES
    p_num  = number_crabs.

LOOP AT string_crabs ASSIGNING FIELD-SYMBOL(<crab>).
  fuel = fuel + abs( <crab> - median ).
ENDLOOP.

WRITE: |{ fuel }|.
