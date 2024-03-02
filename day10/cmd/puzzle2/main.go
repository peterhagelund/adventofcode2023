package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"slices"
	"strings"
)

type coord struct {
	y int
	x int
}

func main() {
	file, err := os.Open("puzzle_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	maze := make([][]rune, 0)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		maze = append(maze, []rune(scanner.Text()))
	}
	y, x := findStart(maze)
	if y == -1 || x == -1 {
		log.Fatal("no 'S' found in maze")
	}
	count := calculateInsideTileCount(maze, y, x)
	fmt.Printf("count = %d\n", count)
}

func findStart(maze [][]rune) (int, int) {
	for y := 0; y < len(maze); y++ {
		x := slices.Index(maze[y], 'S')
		if x != -1 {
			return y, x
		}
	}
	return -1, -1
}

func calculateInsideTileCount(maze [][]rune, y, x int) int {
	height := len(maze)
	width := len(maze[0])
	start := coord{y, x}
	queue := make([]coord, 1)
	queue[0] = start
	moves := make(map[coord]bool)
	moves[start] = true
	actualS := "|-JL7F"

	for len(queue) > 0 {
		pos := queue[0]
		queue = queue[1:]
		r := maze[pos.y][pos.x]
		var ok bool
		if pos.y > 0 {
			above := coord{pos.y - 1, pos.x}
			_, ok = moves[above]
			if !ok && strings.ContainsRune("S|JL", r) && strings.ContainsRune("|7F", maze[above.y][above.x]) {
				moves[above] = true
				queue = append(queue, above)
				if r == 'S' {
					actualS = retainCandidates(actualS, "|JL")
				}
			}
		}
		if pos.y < height-1 {
			below := coord{pos.y + 1, pos.x}
			_, ok = moves[below]
			if !ok && strings.ContainsRune("S|7F", r) && strings.ContainsRune("|JL", maze[below.y][below.x]) {
				moves[below] = true
				queue = append(queue, below)
				if r == 'S' {
					actualS = retainCandidates(actualS, "|7F")
				}
			}
		}
		if pos.x > 0 {
			left := coord{pos.y, pos.x - 1}
			_, ok = moves[left]
			if !ok && strings.ContainsRune("S-J7", r) && strings.ContainsRune("-LF", maze[left.y][left.x]) {
				moves[left] = true
				queue = append(queue, left)
				if r == 'S' {
					actualS = retainCandidates(actualS, "-J7")
				}
			}
		}
		if pos.x < width-1 {
			right := coord{pos.y, pos.x + 1}
			_, ok = moves[right]
			if !ok && strings.ContainsRune("S-LF", r) && strings.ContainsRune("-J7", maze[right.y][right.x]) {
				moves[right] = true
				queue = append(queue, right)
				if r == 'S' {
					actualS = retainCandidates(actualS, "-LF")
				}
			}
		}
	}
	maze[y][x] = []rune(actualS)[0]
	for y = 0; y < height; y++ {
		for x = 0; x < width; x++ {
			if _, ok := moves[coord{y, x}]; !ok {
				maze[y][x] = '.'
			}
		}
	}
	outsideTiles := map[coord]bool{}
	for y = 0; y < height; y++ {
		outside := true
		vertical := false
		for x = 0; x < width; x++ {
			r := maze[y][x]
			switch {
			case r == '|':
				outside = !outside
			case r == 'L' || r == 'F':
				vertical = r == 'L'
			case r == '7' || r == 'J':
				end := '7'
				if vertical {
					end = 'J'
				}
				if r != end {
					outside = !outside
				}
				vertical = false
			}
			if outside {
				outsideTiles[coord{y, x}] = true
			}
		}
	}
	for pos := range moves {
		outsideTiles[pos] = true
	}
	return height*width - len(outsideTiles)
}

func retainCandidates(actualS string, candidates string) string {
	return strings.Map(func(r rune) rune {
		if strings.ContainsRune(candidates, r) {
			return r
		}
		return -1
	}, actualS)
}
