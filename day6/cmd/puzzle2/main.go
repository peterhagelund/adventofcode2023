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
	var time int
	var distance int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		parts := strings.Split(scanner.Text(), ":")
		switch parts[0] {
		case "Time":
			time = number(parts[1])
		case "Distance":
			distance = number(parts[1])
		default:
			log.Fatal(parts[1])
		}
	}
	options := 0
	for holdTime := 0; holdTime < time; holdTime++ {
		speed := holdTime
		d := (time - holdTime) * speed
		if d > distance {
			options++
		}
	}
	fmt.Printf("options = %d\n", options)
}

func number(s string) int {
	n, err := strconv.Atoi(strings.ReplaceAll(s, " ", ""))
	if err != nil {
		log.Fatal(err)
	}
	return n
}
