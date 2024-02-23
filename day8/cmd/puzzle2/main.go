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
	locations := make([]string, 0)
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
			location := []rune(parts[0])
			if location[2] == 'A' {
				locations = append(locations, parts[0])
			}
		}
	}
	repeats := make([]int, 0)
	for _, location := range locations {
		results := findRepeatCycle(location, instructions, network)
		if results[1]%results[0] != 0 {
			log.Fatal("location does not repeat")
		}
		repeats = append(repeats, results[0])
	}
	steps := lcm(repeats...)
	fmt.Printf("steps = %d\n", steps)
}

func findRepeatCycle(location string, instructions []rune, network map[string][2]string) []int {
	ip := -1
	steps := 0
	results := make([]int, 0)
	for len(results) < 2 {
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
		if strings.HasSuffix(location, "Z") {
			results = append(results, steps)
		}
	}
	return results
}

func lcm(numbers ...int) int {
	result := numbers[0] * numbers[1] / gcd(numbers[0], numbers[1])
	for i := 2; i < len(numbers); i++ {
		result = lcm(result, numbers[i])
	}
	return result
}

func gcd(a, b int) int {
	for b != 0 {
		t := b
		b = a % b
		a = t
	}
	return a
}
