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
	sum := 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		fields := strings.Fields(scanner.Text())
		values := make([]int, len(fields))
		for i, field := range fields {
			value, err := strconv.Atoi(field)
			if err != nil {
				log.Fatal(err)
			}
			values[i] = value
		}
		sum += extrapolate(values)
	}
	fmt.Printf("sum = %d\n", sum)
}

func extrapolate(values []int) int {
	sequences := make([][]int, 0)
	sequence := values
	for {
		sequences = append(sequences, sequence)
		if slices.Min(sequence) == 0 && slices.Max(sequence) == 0 {
			break
		}
		differences := make([]int, 0)
		for i := len(sequence) - 1; i > 0; i-- {
			difference := sequence[i] - sequence[i-1]
			differences = append([]int{difference}, differences...)
		}
		sequence = differences
	}
	first := 0
	for i := len(sequences) - 1; i >= 0; i-- {
		sequence = sequences[i]
		if i < len(sequences)-1 {
			first = sequence[0] - first
		}
		sequences[i] = append([]int{first}, sequence...)
	}
	return first
}
