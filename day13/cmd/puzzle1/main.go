package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"reflect"
	"slices"
)

func main() {
	file, err := os.Open("puzzle_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	patterns := make([][]rune, 0)
	sum := 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		text := scanner.Text()
		if len(text) > 0 {
			patterns = append(patterns, []rune(text))
		} else {
			sum += processPatterns(patterns)
			patterns = make([][]rune, 0)
		}
	}
	if len(patterns) > 0 {
		sum += processPatterns(patterns)
	}
	fmt.Printf("sum = %d\n", sum)
}

func processPatterns(patterns [][]rune) int {
	result := 0
	result += findReflection(patterns) * 100
	flipped := make([][]rune, len(patterns[0]))
	for x := 0; x < len(patterns[0]); x++ {
		flipped[x] = make([]rune, len(patterns))
		for y := 0; y < len(patterns); y++ {
			flipped[x][y] = patterns[y][x]
		}
	}
	result += findReflection(flipped)
	return result
}

func findReflection(patterns [][]rune) int {
	for row := 1; row < len(patterns); row++ {
		above := slices.Clone(patterns[:row])
		slices.Reverse(above)
		below := slices.Clone(patterns[row:])
		size := min(len(above), len(below))
		if reflect.DeepEqual(above[:size], below[:size]) {
			return row
		}
	}
	return 0
}
