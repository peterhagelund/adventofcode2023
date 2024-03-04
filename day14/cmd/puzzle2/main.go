package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"slices"
)

func main() {
	file, err := os.Open("puzzle_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	platform := make([][]rune, 0)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		platform = append(platform, []rune(scanner.Text()))
	}
	loads := make([]int, 0)
	unique := make(map[int]bool)
	tilts := []func([][]rune){tiltNorth, tiltWest, tiltSouth, tiltEast}
	for {
		for _, f := range tilts {
			f(platform)
		}
		load := calculateLoad(platform)
		loads = append(loads, load)
		unique[load] = true
		if len(unique) < len(loads) {
			break
		}
	}
	repeat := loads[len(loads)-1]
	index := slices.Index(loads, repeat)
	cycle := len(loads) - index - 1
	offset := (999999999 - index) % cycle
	load := loads[index+offset]
	fmt.Printf("load = %d\n", load)
}

func tiltNorth(platform [][]rune) {
	for y := 0; y < len(platform); y++ {
		for x := 0; x < len(platform[0]); x++ {
			if platform[y][x] != 'O' {
				continue
			}
			_y := y
			for _y > 0 && platform[_y-1][x] == '.' {
				platform[_y-1][x] = 'O'
				platform[_y][x] = '.'
				_y--
			}
		}
	}
}

func tiltWest(platform [][]rune) {
	for x := 0; x < len(platform[0]); x++ {
		for y := 0; y < len(platform); y++ {
			if platform[y][x] != 'O' {
				continue
			}
			_x := x
			for _x > 0 && platform[y][_x-1] == '.' {
				platform[y][_x-1] = 'O'
				platform[y][_x] = '.'
				_x--
			}
		}
	}
}

func tiltSouth(platform [][]rune) {
	for y := len(platform) - 2; y >= 0; y-- {
		for x := 0; x < len(platform[0]); x++ {
			if platform[y][x] != 'O' {
				continue
			}
			_y := y
			for _y < len(platform)-1 && platform[_y+1][x] == '.' {
				platform[_y+1][x] = 'O'
				platform[_y][x] = '.'
				_y++
			}
		}
	}
}

func tiltEast(platform [][]rune) {
	for x := len(platform[0]) - 2; x >= 0; x-- {
		for y := 0; y < len(platform); y++ {
			if platform[y][x] != 'O' {
				continue
			}
			_x := x
			for _x < len(platform[0])-1 && platform[y][_x+1] == '.' {
				platform[y][_x+1] = 'O'
				platform[y][_x] = '.'
				_x++
			}
		}
	}
}

func calculateLoad(platform [][]rune) int {
	load := 0
	for y := 0; y < len(platform); y++ {
		for x := 0; x < len(platform[0]); x++ {
			if platform[y][x] == 'O' {
				load += len(platform) - y
			}
		}
	}
	return load
}
