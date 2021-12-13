REPORT z_advent_code_2021_10_1.
TYPES: BEGIN OF penalties_line,
         char    TYPE c,
         penalty TYPE i,
       END OF penalties_line,

       BEGIN OF chunk_pair,
         opener TYPE c,
         closer TYPE c,
       END OF chunk_pair.
DATA:
  input_lines       TYPE TABLE OF string,
  char_offset       TYPE i,
  opened_chunks     TYPE TABLE OF c,
  current_char      TYPE c,
  last_opened_chunk TYPE c,
  score             TYPE i,
  penalties         TYPE TABLE OF penalties_line,
  chunk_pairs       TYPE TABLE OF chunk_pair.

cl_gui_frontend_services=>gui_upload( EXPORTING filename = 'C:\Data\AdventOfCode\Day10input.txt'
                                      CHANGING  data_tab = input_lines ).

penalties = VALUE #( ( char = ')' penalty = 3 )
                      ( char = ']' penalty = 57 )
                      ( char = '}' penalty = 1197 )
                      ( char = '>' penalty = 25137 ) ).
chunk_pairs = VALUE #( ( opener = '(' closer = ')' )
                        ( opener = '<' closer = '>' )
                        ( opener = '[' closer = ']' )
                        ( opener = '{' closer = '}' ) ).

LOOP AT input_lines INTO DATA(input_line).
  DO strlen( input_line ) TIMES.
    char_offset = sy-index - 1.
    current_char = input_line+char_offset(1).
    IF current_char CA '(<[{'.
      INSERT current_char INTO opened_chunks INDEX 1.
    ELSE.
      last_opened_chunk = opened_chunks[ 1 ].
      IF current_char = chunk_pairs[ opener = last_opened_chunk ]-closer.
        DELETE opened_chunks INDEX 1.
      ELSE.
        score = score + penalties[ char = current_char ]-penalty   .
        EXIT.
      ENDIF.
    ENDIF.
  ENDDO.
ENDLOOP.
WRITE: |{ score }|.
