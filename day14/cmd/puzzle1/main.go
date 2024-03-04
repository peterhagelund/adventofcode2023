package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
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
	tiltPlatform(platform)
	load := calculateLoad(platform)
	fmt.Printf("load = %d\n", load)
}

func tiltPlatform(platform [][]rune) {
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
