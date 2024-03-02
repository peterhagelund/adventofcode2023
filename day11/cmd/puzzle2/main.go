package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"slices"
)

type coord struct {
	x int
	y int
}

type pair struct {
	g1 int
	g2 int
}

func main() {
	file, err := os.Open("puzzle_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	space := make([][]rune, 0)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		space = append(space, []rune(scanner.Text()))
	}
	rows, columns := getSpaceExpansion(space)
	galaxyMap := buildGalaxyMap(space, rows, columns, 1000000)
	galaxyPairs := buildGalaxyPairs(len(galaxyMap))
	sum := 0
	for _, galaxyPair := range galaxyPairs {
		sum += calculateDistance(galaxyMap, galaxyPair)
	}
	fmt.Printf("sum = %d\n", sum)
}

func getSpaceExpansion(space [][]rune) ([]int, []int) {
	height := len(space)
	width := len(space[0])
	rows := make([]int, 0)
	for y := 0; y < height; y++ {
		if !slices.Contains(space[y], '#') {
			rows = append(rows, y)
		}
	}
	columns := make([]int, 0)
	for x := 0; x < width; x++ {
		count := 0
		for y := 0; y < height; y++ {
			if space[y][x] == '#' {
				count++
			}
		}
		if count == 0 {
			columns = append(columns, x)
		}
	}
	return rows, columns
}

func buildGalaxyMap(space [][]rune, rows, columns []int, factor int) map[int]coord {
	height := len(space)
	width := len(space[0])
	galaxyMap := make(map[int]coord)
	num := 0
	_y := 0
	for y := 0; y < height; y++ {
		if slices.Contains(rows, y) {
			_y += factor
		} else {
			_x := 0
			for x := 0; x < width; x++ {
				if slices.Contains(columns, x) {
					_x += factor
				} else {
					if space[y][x] == '#' {
						galaxyMap[num] = coord{_y, _x}
						num++
					}
					_x++
				}
			}
			_y++
		}
	}
	return galaxyMap
}

func buildGalaxyPairs(count int) []pair {
	pairs := make([]pair, 0)
	for g1 := 0; g1 < count; g1++ {
		for g2 := g1 + 1; g2 < count; g2++ {
			pairs = append(pairs, pair{g1, g2})
		}
	}
	return pairs
}

func calculateDistance(galaxyMap map[int]coord, galaxyPair pair) int {
	pos0 := galaxyMap[galaxyPair.g1]
	pos1 := galaxyMap[galaxyPair.g2]
	return int(math.Abs(float64(pos0.y)-float64(pos1.y)) + math.Abs(float64(pos0.x)-float64(pos1.x)))
}
