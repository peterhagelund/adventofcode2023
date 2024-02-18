package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
)

func main() {
	file, err := os.Open("puzzle_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	re := regexp.MustCompile("[0-9]")
	sum := 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		matches := re.FindAllString(scanner.Text(), -1)
		if matches != nil {
			sum += int(matches[0][0]-'0')*10 + int(matches[len(matches)-1][0]-'0')
		}
	}
	fmt.Printf("sum = %d\n", sum)
}
