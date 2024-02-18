package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

var digits = []string{"1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}

func main() {
	file, err := os.Open("puzzle_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	sum := 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		text := scanner.Text()
		first := 0
		first_index := len(text)
		last := 0
		last_index := 0
		for i, d := range digits {
			index := strings.Index(text, d)
			if index == -1 {
				continue
			}
			if index < first_index {
				first = i%(len(digits)/2) + 1
				first_index = index
			}
			index = strings.LastIndex(text, d)
			if index >= last_index {
				last = i%(len(digits)/2) + 1
				last_index = index
			}
		}
		sum += first*10 + last
	}
	fmt.Printf("sum = %d\n", sum)
}
