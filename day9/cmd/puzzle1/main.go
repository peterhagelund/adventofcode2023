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
		for i := 0; i < len(sequence)-1; i++ {
			difference := sequence[i+1] - sequence[i]
			differences = append(differences, difference)
		}
		sequence = differences
	}
	last := 0
	for i := len(sequences) - 1; i >= 0; i-- {
		sequence = sequences[i]
		if i < len(sequences)-1 {
			last = sequence[len(sequence)-1] + last
		}
		sequences[i] = append(sequence, last)
	}
	return last
}
