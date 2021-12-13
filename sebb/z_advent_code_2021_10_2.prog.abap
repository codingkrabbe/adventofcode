REPORT z_advent_code_2021_10_2.
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
  score             TYPE int8,
  penalties         TYPE TABLE OF penalties_line,
  penalty_results   TYPE TABLE OF int8,
  current_penalty   TYPE int8,
  median_index      TYPE i,
  chunk_pairs       TYPE TABLE OF chunk_pair.

cl_gui_frontend_services=>gui_upload( EXPORTING filename = 'C:\Data\AdventOfCode\Day10input.txt'
                                      CHANGING  data_tab = input_lines ).

penalties = VALUE #( ( char = ')' penalty = 1 )
                      ( char = ']' penalty = 2 )
                      ( char = '}' penalty = 3 )
                      ( char = '>' penalty = 4 ) ).
chunk_pairs = VALUE #( ( opener = '(' closer = ')' )
                        ( opener = '<' closer = '>' )
                        ( opener = '[' closer = ']' )
                        ( opener = '{' closer = '}' ) ).

LOOP AT input_lines INTO DATA(input_line).
  DATA(line_corrupt) = abap_false.
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
        CLEAR opened_chunks.
        line_corrupt = abap_true.
        EXIT.
      ENDIF.
    ENDIF.
  ENDDO.
  IF line_corrupt <> abap_true.
    CLEAR current_penalty.
    LOOP AT opened_chunks INTO last_opened_chunk.
      current_penalty = current_penalty * 5 + penalties[ char = chunk_pairs[ opener = last_opened_chunk ]-closer ]-penalty.
    ENDLOOP.
    CLEAR opened_chunks.
    APPEND current_penalty TO penalty_results.
  ENDIF.
ENDLOOP.

SORT penalty_results.
median_index = round( val = ( lines( penalty_results ) / 2 ) dec = 0 ).
score = penalty_results[ median_index ].
WRITE: |{ score }|.
