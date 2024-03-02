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

type fooer interface {
	frobnicate(i int) bool
}

type foo struct {
}

func (f foo) frobnicate(i int) bool {
	return false
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
	f := &foo{}
	i := createThing[foo]()
	fmt.Println(f, i)
}

func createThing[T fooer]() T {
	var t T
	return t
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
	// actualS := []rune{'|', '-', 'J', 'L', '7', 'F'}

	for len(queue) > 0 {
		pos := queue[0]
		queue = queue[1:]
		r := maze[pos.y][pos.x]
		var ok bool
		if pos.y > 0 {
			above := coord{y: pos.y - 1, x: pos.x}
			_, ok = moves[above]
			if !ok && strings.ContainsRune("S|JL", r) && strings.ContainsRune("|7F", maze[above.y][above.x]) {
				moves[above] = true
				queue = append(queue, above)
			}
		}
		if pos.y < height-1 {
			below := coord{y: pos.y + 1, x: pos.x}
			_, ok = moves[below]
			if !ok && strings.ContainsRune("S|7F", r) && strings.ContainsRune("|JL", maze[below.y][below.x]) {
				moves[below] = true
				queue = append(queue, below)
			}
		}
		if pos.x > 0 {
			left := coord{y: pos.y, x: pos.x - 1}
			_, ok = moves[left]
			if !ok && strings.ContainsRune("S-J7", r) && strings.ContainsRune("-LF", maze[left.y][left.x]) {
				moves[left] = true
				queue = append(queue, left)
			}
		}
		if pos.x < width-1 {
			right := coord{y: pos.y, x: pos.x + 1}
			_, ok = moves[right]
			if !ok && strings.ContainsRune("S-LF", r) && strings.ContainsRune("-J7", maze[right.y][right.x]) {
				moves[right] = true
				queue = append(queue, right)
			}
		}
	}
	return len(moves) / 2
}
