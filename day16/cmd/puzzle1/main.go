package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"slices"
	"strings"
)

type direction int

const (
	right direction = iota
	down
	left
	up
)

type leg struct {
	y int
	x int
	d direction
}

func main() {
	file, err := os.Open("puzzle_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	contraption := make([][]rune, 0)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		contraption = append(contraption, []rune(scanner.Text()))
	}
	tileCount := calculateEnergizedTiles(contraption, leg{0, 0, right})
	fmt.Printf("energized tiles = %d\n", tileCount)
}

func calculateEnergizedTiles(contraption [][]rune, start leg) int {
	legs := make(map[leg]bool)
	energized := make([][]bool, len(contraption))
	for y, row := range contraption {
		energized[y] = make([]bool, len(row))
		for x := range row {
			energized[y][x] = false
		}
	}
	queue := make([]leg, 1)
	queue[0] = start
	height := len(contraption)
	width := len(contraption[0])
	for len(queue) > 0 {
		l := queue[0]
		queue = slices.Delete(queue, 0, 1)
		if _, ok := legs[l]; ok {
			continue
		}
		legs[l] = true
		y, x, d := l.y, l.x, l.d
		done := false
		for !done {
			energized[y][x] = true
			tile := contraption[y][x]
			switch d {
			case right:
				if strings.ContainsRune(".-", tile) {
					x++
					done = x == width
				} else {
					if y > 0 && strings.ContainsRune("|/", tile) {
						queue = append(queue, leg{y - 1, x, up})
					}
					if y+1 < height && strings.ContainsRune("|\\", tile) {
						queue = append(queue, leg{y + 1, x, down})
					}
					done = true
				}
			case down:
				if strings.ContainsRune(".|", tile) {
					y++
					done = y == height
				} else {
					if x > 0 && strings.ContainsRune("-/", tile) {
						queue = append(queue, leg{y, x - 1, left})
					}
					if x+1 < width && strings.ContainsRune("-\\", tile) {
						queue = append(queue, leg{y, x + 1, right})
					}
					done = true
				}
			case left:
				if strings.ContainsRune(".-", tile) {
					x--
					done = x < 0
				} else {
					if y > 0 && strings.ContainsRune("|\\", tile) {
						queue = append(queue, leg{y - 1, x, up})
					}
					if y+1 < height && strings.ContainsRune("|/", tile) {
						queue = append(queue, leg{y + 1, x, down})
					}
					done = true
				}
			case up:
				if strings.ContainsRune(".|", tile) {
					y--
					done = y < 0
				} else {
					if x > 0 && strings.ContainsRune("-\\", tile) {
						queue = append(queue, leg{y, x - 1, left})
					}
					if x+1 < width && strings.ContainsRune("-/", tile) {
						queue = append(queue, leg{y, x + 1, right})
					}
					done = true
				}
			}
		}
	}
	sum := 0
	for _, row := range energized {
		for _, on := range row {
			if on {
				sum++
			}
		}
	}
	return sum
}
