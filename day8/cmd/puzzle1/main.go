package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strings"
)

func main() {
	file, err := os.Open("puzzle_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	re := regexp.MustCompile("[A-Z]{3}")
	var instructions []rune
	network := make(map[string][2]string)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		text := scanner.Text()
		if len(text) == 0 {
			continue
		}
		if !strings.ContainsRune(text, '=') {
			instructions = []rune(text)
		} else {
			parts := re.FindAllString(text, -1)
			network[parts[0]] = [2]string{parts[1], parts[2]}
		}
	}
	steps := 0
	location := "AAA"
	ip := -1
	for location != "ZZZ" {
		steps++
		ip++
		if ip >= len(instructions) {
			ip = 0
		}
		instruction := instructions[ip]
		leftOrRight := network[location]
		if instruction == 'L' {
			location = leftOrRight[0]
		} else {
			location = leftOrRight[1]
		}
	}
	fmt.Printf("steps = %d\n", steps)
}
