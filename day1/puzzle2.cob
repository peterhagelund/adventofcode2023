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
       01  FILE-STATUS             PIC X(2).
       01  LINE-NO                 PIC 9(6) VALUE ZERO.
       01  SUM-OF-ALL-DIGITS       PIC 9(6) VALUE ZERO.
       01  SUM-OF-DIGITS           PIC 9(4).
       01  DIGIT-STATUS            PIC X.
           88 DIGIT-FOUND          VALUE "T" WHEN SET TO FALSE IS "F".
           88 DIGIT-NOT-FOUND      VALUE "F".
       01  R-IDX                   PIC 9(2).
       01  MAX-IDX                 PIC 9(2).
       01  D-IDX                   PIC 9(2).
       01  FIRST-IDX               PIC 9(2).
       01  FIRST-DIGIT             PIC 9.
       01  LAST-IDX                PIC 9(2).
       01  LAST-DIGIT              PIC 9.
       01  DIGITS.
           03  FILLER              PIC X(5) VALUE "0".
           03  FILLER              PIC 9 VALUE 1.
           03  FILLER              PIC 9 VALUE 0.
           03  FILLER              PIC X(5) VALUE "1".
           03  FILLER              PIC 9 VALUE 1.
           03  FILLER              PIC 9 VALUE 1.
           03  FILLER              PIC X(5) VALUE "2".
           03  FILLER              PIC 9 VALUE 1.
           03  FILLER              PIC 9 VALUE 2.
           03  FILLER              PIC X(5) VALUE "3".
           03  FILLER              PIC 9 VALUE 1.
           03  FILLER              PIC 9 VALUE 3.
           03  FILLER              PIC X(5) VALUE "4".
           03  FILLER              PIC 9 VALUE 1.
           03  FILLER              PIC 9 VALUE 4.
           03  FILLER              PIC X(5) VALUE "5".
           03  FILLER              PIC 9 VALUE 1.
           03  FILLER              PIC 9 VALUE 5.
           03  FILLER              PIC X(5) VALUE "6".
           03  FILLER              PIC 9 VALUE 1.
           03  FILLER              PIC 9 VALUE 6.
           03  FILLER              PIC X(5) VALUE "7".
           03  FILLER              PIC 9 VALUE 1.
           03  FILLER              PIC 9 VALUE 7.
           03  FILLER              PIC X(5) VALUE "8".
           03  FILLER              PIC 9 VALUE 1.
           03  FILLER              PIC 9 VALUE 8.
           03  FILLER              PIC X(5) VALUE "9".
           03  FILLER              PIC 9 VALUE 1.
           03  FILLER              PIC 9 VALUE 9.
           03  FILLER              PIC X(5) VALUE "zero".
           03  FILLER              PIC 9 VALUE 4.
           03  FILLER              PIC 9 VALUE 0.
           03  FILLER              PIC X(5) VALUE "one".
           03  FILLER              PIC 9 VALUE 3.
           03  FILLER              PIC 9 VALUE 1.
           03  FILLER              PIC X(5) VALUE "two".
           03  FILLER              PIC 9 VALUE 3.
           03  FILLER              PIC 9 VALUE 2.
           03  FILLER              PIC X(5) VALUE "three".
           03  FILLER              PIC 9 VALUE 5.
           03  FILLER              PIC 9 VALUE 3.
           03  FILLER              PIC X(5) VALUE "four".
           03  FILLER              PIC 9 VALUE 4.
           03  FILLER              PIC 9 VALUE 4.
           03  FILLER              PIC X(5) VALUE "five".
           03  FILLER              PIC 9 VALUE 4.
           03  FILLER              PIC 9 VALUE 5.
           03  FILLER              PIC X(5) VALUE "six".
           03  FILLER              PIC 9 VALUE 3.
           03  FILLER              PIC 9 VALUE 6.
           03  FILLER              PIC X(5) VALUE "seven".
           03  FILLER              PIC 9 VALUE 5.
           03  FILLER              PIC 9 VALUE 7.
           03  FILLER              PIC X(5) VALUE "eight".
           03  FILLER              PIC 9 VALUE 5.
           03  FILLER              PIC 9 VALUE 8.
           03  FILLER              PIC X(5) VALUE "nine".
           03  FILLER              PIC 9 VALUE 4.
           03  FILLER              PIC 9 VALUE 9.
       01  REDEFINES DIGITS.
           03  DIGIT OCCURS 20.
               05  DIGIT-TEXT      PIC X(5).
               05  DIGIT-LEN       PIC 9.
               05  DIGIT-VALUE     PIC 9.
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
           MOVE ZERO TO LAST-IDX.
           MOVE 80 TO FIRST-IDX.
           PERFORM VARYING R-IDX FROM 1 BY 1 UNTIL R-IDX > 80
               PERFORM VARYING D-IDX FROM 1 BY 1 UNTIL D-IDX > 20
                   PERFORM CHECK-DIGIT
               END-PERFORM
           END-PERFORM.
           IF NOT DIGIT-FOUND THEN
               EXIT SECTION
           END-IF.
           COMPUTE SUM-OF-DIGITS = FIRST-DIGIT * 10 + LAST-DIGIT.
           ADD SUM-OF-DIGITS TO SUM-OF-ALL-DIGITS.

       CHECK-DIGIT SECTION.
           COMPUTE MAX-IDX = 80 - DIGIT-LEN(D-IDX).
           IF R-IDX > MAX-IDX THEN
               EXIT SECTION
           END-IF.
           IF PUZZLE-RECORD(R-IDX:DIGIT-LEN(D-IDX)) = 
               DIGIT-TEXT(D-IDX)(1:DIGIT-LEN(D-IDX)) THEN
               SET DIGIT-FOUND TO TRUE
               IF R-IDX < FIRST-IDX THEN
                   MOVE R-IDX TO FIRST-IDX
                   MOVE DIGIT-VALUE(D-IDX) TO FIRST-DIGIT
               END-IF
               IF R-IDX > LAST-IDX THEN
                   MOVE R-IDX TO LAST-IDX
                   MOVE DIGIT-VALUE(D-IDX) TO LAST-DIGIT
               END-IF
           END-IF.
