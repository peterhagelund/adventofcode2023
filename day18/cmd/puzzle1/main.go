package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type step struct {
	direction rune
	distance  int
	color     string
}

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
	plan := make([]*step, 0)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		fields := strings.Fields(scanner.Text())
		direction := []rune(fields[0])[0]
		distance, err := strconv.Atoi(fields[1])
		if err != nil {
			log.Fatal(err)
		}
		color := fields[2]
		plan = append(plan, &step{direction, distance, color})
	}
	height, width, y, x := determineLagoonDimensions(plan)
	lagoon := make([][]rune, height)
	for i := range lagoon {
		lagoon[i] = make([]rune, width)
		for j := range lagoon[i] {
			lagoon[i][j] = '.'
		}
	}
	populateLagoon(lagoon, plan, y, x)
	moves := determineMoves(lagoon, y, x)
	insideTiles := determineInsideTiles(lagoon)
	total := make(map[coord]bool)
	for _, c := range moves {
		total[*c] = true
	}
	for _, c := range insideTiles {
		total[*c] = true
	}
	fmt.Println(len(total))
}

func determineLagoonDimensions(plan []*step) (int, int, int, int) {
	y, x := 0, 0
	min_x, max_x := x, x
	min_y, max_y := y, y
	for _, s := range plan {
		direction := s.direction
		distance := s.distance
		switch direction {
		case 'R':
			x += distance
		case 'D':
			y += distance
		case 'L':
			x -= distance
		case 'U':
			y -= distance
		default:
			log.Fatal(direction)
		}
		min_y = min(min_y, y)
		max_y = max(max_y, y)
		min_x = min(min_x, x)
		max_x = max(max_x, x)
	}
	height := (max_y - min_y) + 1
	width := (max_x - min_x) + 1
	y, x = 0-min_y, 0-min_x
	return height, width, y, x
}

func populateLagoon(lagoon [][]rune, plan []*step, y, x int) {
	prev := ' '
	for _, s := range plan {
		direction := s.direction
		distance := s.distance
		switch direction {
		case 'R':
			for i := 0; i < distance; i++ {
				if i == 0 {
					if prev == 'D' {
						lagoon[y][x] = 'L'
					} else {
						lagoon[y][x] = 'F'
					}
				} else {
					lagoon[y][x] = '-'
				}
				x++
			}
		case 'D':
			for i := 0; i < distance; i++ {
				if i == 0 {
					if prev == 'R' {
						lagoon[y][x] = '7'
					} else {
						lagoon[y][x] = 'F'
					}
				} else {
					lagoon[y][x] = '|'
				}
				y++
			}
		case 'L':
			for i := 0; i < distance; i++ {
				if i == 0 {
					if prev == 'U' {
						lagoon[y][x] = '7'
					} else {
						lagoon[y][x] = 'J'
					}
				} else {
					lagoon[y][x] = '-'
				}
				x--
			}
		case 'U':
			for i := 0; i < distance; i++ {
				if i == 0 {
					if prev == 'R' {
						lagoon[y][x] = 'J'
					} else {
						lagoon[y][x] = 'L'
					}
				} else {
					lagoon[y][x] = '|'
				}
				y--
			}
		default:
			log.Fatal(direction)
		}
		prev = direction
	}
}

func determineMoves(lagoon [][]rune, y, x int) []*coord {
	height := len(lagoon)
	width := len(lagoon[0])
	start := coord{y, x}
	queue := make([]coord, 1)
	queue[0] = start
	seen := make(map[coord]bool)
	seen[start] = true
	actualS := "|-JL7F"
	moves := make([]*coord, 1)
	moves[0] = &start

	for len(queue) > 0 {
		pos := queue[0]
		queue = queue[1:]
		r := lagoon[pos.y][pos.x]
		var ok bool
		if pos.y > 0 {
			above := coord{pos.y - 1, pos.x}
			_, ok = seen[above]
			if !ok && strings.ContainsRune("S|JL", r) && strings.ContainsRune("|7F", lagoon[above.y][above.x]) {
				seen[above] = true
				queue = append(queue, above)
				moves = append(moves, &above)
				if r == 'S' {
					actualS = retainCandidates(actualS, "|JL")
				}
			}
		}
		if pos.y < height-1 {
			below := coord{pos.y + 1, pos.x}
			_, ok = seen[below]
			if !ok && strings.ContainsRune("S|7F", r) && strings.ContainsRune("|JL", lagoon[below.y][below.x]) {
				seen[below] = true
				queue = append(queue, below)
				moves = append(moves, &below)
				if r == 'S' {
					actualS = retainCandidates(actualS, "|7F")
				}
			}
		}
		if pos.x > 0 {
			left := coord{pos.y, pos.x - 1}
			_, ok = seen[left]
			if !ok && strings.ContainsRune("S-J7", r) && strings.ContainsRune("-LF", lagoon[left.y][left.x]) {
				seen[left] = true
				queue = append(queue, left)
				moves = append(moves, &left)
				if r == 'S' {
					actualS = retainCandidates(actualS, "-J7")
				}
			}
		}
		if pos.x < width-1 {
			right := coord{pos.y, pos.x + 1}
			_, ok = seen[right]
			if !ok && strings.ContainsRune("S-LF", r) && strings.ContainsRune("-J7", lagoon[right.y][right.x]) {
				seen[right] = true
				queue = append(queue, right)
				moves = append(moves, &right)
				if r == 'S' {
					actualS = retainCandidates(actualS, "-LF")
				}
			}
		}
	}
	return moves
}

func retainCandidates(actualS string, candidates string) string {
	return strings.Map(func(r rune) rune {
		if strings.ContainsRune(candidates, r) {
			return r
		}
		return -1
	}, actualS)
}

func determineInsideTiles(lagoon [][]rune) []*coord {
	insideTiles := make([]*coord, 0)
	for y, row := range lagoon {
		inside := false
		vertical := false
		for x, r := range row {
			switch r {
			case '|':
				inside = !inside
			case 'L', 'F':
				vertical = r == 'L'
			case '7', 'J':
				if (vertical && r != 'J') || (!vertical && r != '7') {
					inside = !inside
				}
				vertical = false
			}
			if inside {
				insideTiles = append(insideTiles, &coord{y, x})
			}
		}
	}
	return insideTiles
}
