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

type record struct {
	conditions []rune
	sizes      []int
}

func main() {
	file, err := os.Open("puzzle_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	records := make([]record, 0)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		parts := strings.Split(scanner.Text(), " ")
		sizes := make([]int, 0)
		for _, value := range strings.Split(parts[1], ",") {
			size, err := strconv.Atoi(value)
			if err != nil {
				log.Fatal(err)
			}
			sizes = append(sizes, size)
		}
		records = append(records, record{[]rune(parts[0]), sizes})
	}
	sum := 0
	for _, record := range records {
		sum += findArrangements(record, 0, 0, 0)
	}
	fmt.Printf("sum = %d\n", sum)
}

func findArrangements(record record, runeIndex, sizeIndex int, size int) int {
	if runeIndex == len(record.conditions) {
		switch {
		case sizeIndex == len(record.sizes) && size == 0:
			return 1
		case sizeIndex == len(record.sizes)-1 && record.sizes[sizeIndex] == size:
			return 1
		default:
			return 0
		}
	}
	result := 0
	for _, r := range []rune{'.', '#'} {
		if !slices.Contains([]rune{r, '?'}, record.conditions[runeIndex]) {
			continue
		}
		switch {
		case r == '.' && size == 0:
			result += findArrangements(record, runeIndex+1, sizeIndex, 0)
		case r == '.' && size > 0 && sizeIndex < len(record.sizes) && record.sizes[sizeIndex] == size:
			result += findArrangements(record, runeIndex+1, sizeIndex+1, 0)
		case r == '#':
			result += findArrangements(record, runeIndex+1, sizeIndex, size+1)
		}
	}
	return result
}
