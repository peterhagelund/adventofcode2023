package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("puzzle_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	var times []int
	var distances []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		fields := strings.Fields(scanner.Text())
		switch fields[0] {
		case "Time:":
			times = numbers(fields[1:])
		case "Distance:":
			distances = numbers(fields[1:])
		default:
			log.Fatal(fields[0])
		}
	}
	travels := make([]int, 0)
	for i := 0; i < len(times); i++ {
		options := 0
		for holdTime := 0; holdTime < times[i]; holdTime++ {
			speed := holdTime
			distance := (times[i] - holdTime) * speed
			if distance > distances[i] {
				options++
			}
		}
		travels = append(travels, options)
	}
	marginOfError := 1
	for _, travel := range travels {
		marginOfError *= travel
	}
	fmt.Printf("margin of error = %d\n", marginOfError)
}

func numbers(fields []string) []int {
	numbers := make([]int, 0)
	for _, field := range fields {
		n, err := strconv.Atoi(field)
		if err != nil {
			log.Fatal(err)
		}
		numbers = append(numbers, n)
	}
	return numbers
}
