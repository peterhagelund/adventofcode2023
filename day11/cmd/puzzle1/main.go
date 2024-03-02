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
	space = expandSpace(space)
	galaxyMap := buildGalaxyMap(space)
	galaxyPairs := buildGalaxyPairs(len(galaxyMap))
	sum := 0
	for _, galaxyPair := range galaxyPairs {
		sum += calculateDistance(galaxyMap, galaxyPair)
	}
	fmt.Printf("sum = %d\n", sum)
}

func expandSpace(space [][]rune) [][]rune {
	height := len(space)
	width := len(space[0])
	y := 0
	for y < height {
		if !slices.Contains(space[y], '#') {
			space = append(space[:y+1], space[y:]...)
			y++
			height++
		}
		y++
	}
	x := 0
	for x < width {
		count := 0
		for y = 0; y < height; y++ {
			if space[y][x] == '#' {
				count++
			}
		}
		if count == 0 {
			for y = 0; y < height; y++ {
				space[y] = append(space[y][:x+1], space[y][x:]...)
			}
			x++
			width++
		}
		x++
	}
	return space
}

func buildGalaxyMap(space [][]rune) map[int]coord {
	galaxyMap := make(map[int]coord)
	num := 0
	for y, line := range space {
		for x, r := range line {
			if r == '#' {
				galaxyMap[num] = coord{y, x}
				num++
			}
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
