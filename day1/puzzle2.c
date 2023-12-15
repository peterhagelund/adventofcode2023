#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const char *digits[] = {
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
};

int main(int argc, char *argv[]) {
    FILE *input = fopen("puzzle_input.txt", "rt");
    if (input == NULL) {
        return EXIT_FAILURE;
    }
    char line[256] = {0};
    int sum = 0;
    while (fgets(line, sizeof(line), input) != NULL) {
        int first = 0;
        int first_index = strlen(line);
        int last = 0;
        int last_index = -1;
        for (int i = 0; i < 20; i++) {
            if ((i == 0) || (i == 10)) {
                continue;
            }
            int start_index = -1;
            while (true) {
                char *p = strstr(line + start_index + 1, digits[i]);
                if (p == NULL) {
                    break;
                }
                start_index = p - line;
                if (start_index < first_index) {
                    first_index = start_index;
                    first = i % 10;
                }
                if (start_index > last_index) {
                    last_index = start_index;
                    last = i % 10;
                }
            }
        }
        sum += first * 10 + last;
    }
    fclose(input);
    printf("sum = %d\n", sum);
    return EXIT_SUCCESS;
}