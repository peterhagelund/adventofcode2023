       IDENTIFICATION DIVISION.
       PROGRAM-ID. PUZZLE-1.
      * 
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT PUZZLE-FILE ASSIGN TO PUZZLEDD
           ORGANIZATION IS LINE SEQUENTIAL
           ACCESS MODE IS SEQUENTIAL
           FILE STATUS IS FILE-STATUS.
      * 
       DATA DIVISION.
       FILE SECTION.
       FD  PUZZLE-FILE.
       01  PUZZLE-RECORD PIC X(80).
       WORKING-STORAGE SECTION.
       01  FILE-STATUS         PIC X(2).
       01  LINE-NO             PIC 9(6) VALUE ZERO.
       01  SUM-OF-ALL-DIGITS   PIC 9(6) VALUE ZERO.
       01  SUM-OF-DIGITS       PIC 9(4).
       01  IDX                 PIC 9(2).
       01  DIGIT-STATUS        PIC X.
           88 DIGIT-FOUND      VALUE "T" WHEN SET TO FALSE IS "F".
           88 DIGIT-NOT-FOUND  VALUE "F".
       01  FIRST-DIGIT         PIC 9.
       01  LAST-DIGIT          PIC 9.
      *
       PROCEDURE DIVISION.
           PERFORM OPEN-FILE.
           PERFORM READ-FILE.
           PERFORM CLOSE-FILE.
           DISPLAY "SUM = ", SUM-OF-ALL-DIGITS.
           STOP RUN.

       OPEN-FILE SECTION.
           OPEN INPUT PUZZLE-FILE.
           IF FILE-STATUS NOT = "00" THEN
               DISPLAY "FILE OPEN FAILED WITH STATUS ", FILE-STATUS
               STOP RUN
           END-IF.

       READ-FILE SECTION.
           PERFORM UNTIL FILE-STATUS = "10"
               READ PUZZLE-FILE
               IF FILE-STATUS = "00" THEN
                   ADD 1 TO LINE-NO
                   PERFORM FIND-DIGITS
                   IF NOT DIGIT-FOUND THEN
                       DISPLAY "DIGIT(S) NOT FOUND IN ", LINE-NO
                       STOP RUN
                   END-IF
               END-IF
           END-PERFORM.

       CLOSE-FILE SECTION.
           CLOSE PUZZLE-FILE.
           IF FILE-STATUS NOT = "00" THEN
               DISPLAY "FILE CLOSE FAILED WITH STATUS ", FILE-STATUS
               STOP RUN
           END-IF.

       FIND-DIGITS SECTION.
           SET DIGIT-FOUND TO FALSE.
           PERFORM VARYING IDX FROM 1 BY 1
               UNTIL IDX > 80 OR DIGIT-FOUND
               IF PUZZLE-RECORD(IDX:1) IS NUMERIC THEN
                   MOVE PUZZLE-RECORD(IDX:1) TO FIRST-DIGIT
                   SET DIGIT-FOUND TO TRUE
           END-PERFORM.
           IF NOT DIGIT-FOUND THEN
               EXIT SECTION
           END-IF.
           SET DIGIT-FOUND TO FALSE.
           PERFORM VARYING IDX FROM 80 BY -1
               UNTIL IDX = 0 OR DIGIT-FOUND
               IF PUZZLE-RECORD(IDX:1) IS NUMERIC THEN
                   MOVE PUZZLE-RECORD(IDX:1) TO LAST-DIGIT
                   SET DIGIT-FOUND TO TRUE
               END-IF
           END-PERFORM.
           IF NOT DIGIT-FOUND THEN
               EXIT SECTION
           END-IF.
           COMPUTE SUM-OF-DIGITS = FIRST-DIGIT * 10 + LAST-DIGIT.
           ADD SUM-OF-DIGITS TO SUM-OF-ALL-DIGITS.
