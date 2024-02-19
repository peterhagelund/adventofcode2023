package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("puzzle_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	schematic := make([]string, 0)
	for scanner.Scan() {
		schematic = append(schematic, scanner.Text())
	}
	ignorables := ".0123456789"
	re := regexp.MustCompile("[0-9]{1,3}")
	sum := 0
	for lineNo, line := range schematic {
		indexes := re.FindAllStringIndex(line, -1)
		if indexes == nil {
			continue
		}
		for _, match := range indexes {
			start := match[0]
			end := match[1]
			partNo, err := strconv.Atoi(line[start:end])
			if err != nil {
				log.Fatal(err)
			}
			isPart := (start > 0 && strings.IndexByte(ignorables, line[start-1]) == -1) || (end < len(line) && strings.IndexByte(ignorables, line[end]) == -1)
			if !isPart {
				if start > 0 {
					start--
				}
				if end == len(line) {
					end--
				}
				if lineNo > 0 {
					for i := start; i <= end && !isPart; i++ {
						if strings.IndexByte(ignorables, schematic[lineNo-1][i]) == -1 {
							isPart = true
						}
					}
				}
				if !isPart && lineNo < len(schematic)-1 {
					for i := start; i <= end && !isPart; i++ {
						if strings.IndexByte(ignorables, schematic[lineNo+1][i]) == -1 {
							isPart = true
						}
					}
				}
			}
			if isPart {
				sum += partNo
			}
		}
	}
	fmt.Printf("sum = %d\n", sum)
}
