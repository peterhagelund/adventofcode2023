package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Reveal struct {
	Red   *int
	Green *int
	Blue  *int
}
type Game struct {
	ID      int
	Reveals []Reveal
}

func NewReveal(pattern string) *Reveal {
	var red *int = nil
	var green *int = nil
	var blue *int = nil
	color_counts := strings.Split(pattern, ",")
	for _, color_count := range color_counts {
		parts := strings.Split(strings.Trim(color_count, " "), " ")
		count, err := strconv.Atoi(strings.Trim(parts[0], " "))
		if err != nil {
			log.Fatal(err)
		}
		color := parts[1]
		switch color {
		case "red":
			red = &count
		case "green":
			green = &count
		case "blue":
			blue = &count
		default:
			log.Fatal("unknown color")
		}
	}
	return &Reveal{
		Red:   red,
		Green: green,
		Blue:  blue,
	}
}

func (r *Reveal) UpdateMinimums(red *int, green *int, blue *int) {
	if r.Red != nil && *r.Red > *red {
		*red = *r.Red
	}
	if r.Green != nil && *r.Green > *green {
		*green = *r.Green
	}
	if r.Blue != nil && *r.Blue > *blue {
		*blue = *r.Blue
	}
}

func NewGame(text string) *Game {
	parts := strings.Split(text, ":")
	var id int
	fmt.Sscanf(parts[0], "Game %d", &id)
	pattern := strings.Trim(parts[1], " ")
	parts = strings.Split(pattern, ";")
	reveals := make([]Reveal, 0)
	for _, part := range parts {
		pattern = strings.Trim(part, " ")
		reveal := NewReveal(pattern)
		reveals = append(reveals, *reveal)
	}
	return &Game{
		ID:      id,
		Reveals: reveals,
	}
}

func (g *Game) UpdateMinimums(red *int, green *int, blue *int) {
	for _, reveal := range g.Reveals {
		reveal.UpdateMinimums(red, green, blue)
	}
}

func main() {
	file, err := os.Open("puzzle_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	sum := 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		red := 1
		green := 1
		blue := 1
		game := NewGame(scanner.Text())
		game.UpdateMinimums(&red, &green, &blue)
		sum += red * green * blue
	}
	fmt.Printf("sum = %d\n", sum)
}
