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
	counts := make([]int, 0)
	for scanner.Scan() {
		parts := strings.Split(scanner.Text(), ":")
		parts = strings.Split(strings.Trim(parts[1], " "), "|")
		winning_numbers := numbers(parts[0])
		my_numbers := numbers(parts[1])
		count := 0
		for _, n := range my_numbers {
			if slices.Contains(winning_numbers, n) {
				count++
			}
		}
		counts = append(counts, count)
	}
	sum := 0
	for i := 0; i < len(counts); i++ {
		processCard(&sum, counts[i:])
	}
	fmt.Printf("sum = %d\n", sum)
}

func processCard(sum *int, counts []int) {
	*sum++
	for i := 1; i <= counts[0]; i++ {
		processCard(sum, counts[i:])
	}
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
