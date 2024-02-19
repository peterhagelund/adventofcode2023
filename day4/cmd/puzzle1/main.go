package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"slices"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("puzzle_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	sum := 0
	for scanner.Scan() {
		parts := strings.Split(scanner.Text(), ":")
		parts = strings.Split(strings.Trim(parts[1], " "), "|")
		winning_numbers := numbers(parts[0])
		my_numbers := numbers(parts[1])
		value := 0
		for _, n := range my_numbers {
			if slices.Contains(winning_numbers, n) {
				if value == 0 {
					value = 1
				} else {
					value *= 2
				}
			}
		}
		sum += value
	}
	fmt.Printf("sum = %d\n", sum)
}

func numbers(s string) []int {
	numbers := make([]int, 0)
	parts := strings.Split(strings.Trim(s, " "), " ")
	for _, part := range parts {
		part = strings.Trim(part, " ")
		if len(part) == 0 {
			continue
		}
		n, err := strconv.Atoi(part)
		if err != nil {
			log.Fatal(err)
		}
		numbers = append(numbers, n)
	}
	return numbers
}
