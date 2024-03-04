package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	file, err := os.Open("puzzle_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	if !scanner.Scan() {
		log.Fatal("can't read")
	}
	sum := 0
	steps := strings.Split(scanner.Text(), ",")
	for _, step := range steps {
		sum += hash(step)
	}
	fmt.Printf("sum = %d\n", sum)
}

func hash(value string) int {
	h := 0
	for _, b := range value {
		h += int(b)
		h *= 17
		h %= 256
	}
	return h
}
