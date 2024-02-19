package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
)

type Schematic struct {
	Lines   []string
	Matches [][][]int
}

func LoadSchematic(name string) (*Schematic, error) {
	file, err := os.Open(name)
	if err != nil {
		return nil, err
	}
	defer file.Close()
	re := regexp.MustCompile("[0-9]{1,3}")
	lines := make([]string, 0)
	matches := make([][][]int, 0)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		lines = append(lines, line)
		matches = append(matches, re.FindAllStringIndex(line, -1))
	}
	return &Schematic{
		Lines:   lines,
		Matches: matches,
	}, nil
}

func (s *Schematic) Height() int {
	return len(s.Lines)
}

func (s *Schematic) Width() int {
	return len(s.Lines[0])
}

func (s *Schematic) IsGear(y int, x int) bool {
	return s.Lines[y][x] == '*'
}

func (s *Schematic) AdjacentsFor(y int, x int) []int {
	adjacents := make([]int, 0)
	if before := s.AdjancentBefore(y, x); before != -1 {
		adjacents = append(adjacents, before)
	}
	if after := s.AdjacentAfter(y, x); after != -1 {
		adjacents = append(adjacents, after)
	}
	if above := s.AdjacentsAbove(y, x); above != nil {
		adjacents = append(adjacents, above...)
	}
	if below := s.AdjacentsBelow(y, x); below != nil {
		adjacents = append(adjacents, below...)
	}
	return adjacents
}

func (s *Schematic) AdjancentBefore(y int, x int) int {
	for _, match := range s.Matches[y] {
		if x == match[1] {
			value, err := strconv.Atoi(s.Lines[y][match[0]:match[1]])
			if err != nil {
				log.Fatal(err)
			}
			return value
		}
	}
	return -1
}

func (s *Schematic) AdjacentAfter(y int, x int) int {
	for _, match := range s.Matches[y] {
		if x+1 == match[0] {
			value, err := strconv.Atoi(s.Lines[y][match[0]:match[1]])
			if err != nil {
				log.Fatal(err)
			}
			return value
		}
	}
	return -1
}

func (s *Schematic) AdjacentsAbove(y int, x int) []int {
	if y == 0 {
		return nil
	}
	return s.adjacentsNear(y-1, x)
}

func (s *Schematic) AdjacentsBelow(y int, x int) []int {
	if y+1 == len(s.Lines) {
		return nil
	}
	return s.adjacentsNear(y+1, x)
}

func (s *Schematic) adjacentsNear(y int, x int) []int {
	adjacents := make([]int, 0)
	for _, match := range s.Matches[y] {
		if x+1 >= match[0] && x <= match[1] {
			value, err := strconv.Atoi(s.Lines[y][match[0]:match[1]])
			if err != nil {
				log.Fatal(err)
			}
			adjacents = append(adjacents, value)
		}
	}
	return adjacents
}

func main() {
	schematic, err := LoadSchematic("puzzle_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	sum := 0
	for y := 0; y < schematic.Height(); y++ {
		for x := 0; x < schematic.Width(); x++ {
			if !schematic.IsGear(y, x) {
				continue
			}
			adjacents := schematic.AdjacentsFor(y, x)
			if len(adjacents) != 2 {
				continue
			}
			sum += adjacents[0] * adjacents[1]
		}
	}
	fmt.Printf("sum = %d\n", sum)
}
