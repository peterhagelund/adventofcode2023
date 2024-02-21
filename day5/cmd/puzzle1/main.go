package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
)

type MapEntry struct {
	DestinationStart int
	SourceStart      int
	Length           int
}

type Map struct {
	Name       string
	MapEntries []*MapEntry
}

func NewMapEntry(s string) *MapEntry {
	values := numbers(s)
	if len(values) != 3 {
		log.Fatal("wrong map entry length")
	}
	return &MapEntry{
		DestinationStart: values[0],
		SourceStart:      values[1],
		Length:           values[2],
	}
}

func NewMap(name string) *Map {
	mapEntries := make([]*MapEntry, 0)
	return &Map{
		Name:       name,
		MapEntries: mapEntries,
	}
}

func (m *Map) SourceToDest(source int) int {
	for _, mapEntry := range m.MapEntries {
		if source >= mapEntry.SourceStart && source < mapEntry.SourceStart+mapEntry.Length {
			return mapEntry.DestinationStart + (source - mapEntry.SourceStart)
		}
	}
	return source
}

func main() {
	file, err := os.Open("puzzle_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	seeds := make([]int, 0)
	maps := make([]*Map, 0)
	var currentMap *Map
	for scanner.Scan() {
		text := scanner.Text()
		if len(text) == 0 {
			continue
		}
		parts := strings.Split(text, ":")
		if strings.HasSuffix(parts[0], "seeds") {
			seeds = append(seeds, numbers(strings.Trim(parts[1], " "))...)
		} else if strings.HasSuffix(parts[0], "map") {
			name := parts[0][:len(parts[0])-4]
			currentMap = NewMap(name)
			maps = append(maps, currentMap)
		} else {
			mapEntry := NewMapEntry(parts[0])
			currentMap.MapEntries = append(currentMap.MapEntries, mapEntry)
		}
	}
	location := math.MaxInt
	for _, seed := range seeds {
		source := seed
		for _, m := range maps {
			source = m.SourceToDest(source)
		}
		location = min(location, source)
	}
	fmt.Printf("location = %d\n", location)
}

func numbers(s string) []int {
	parts := strings.Split(s, " ")
	values := make([]int, 0)
	for _, part := range parts {
		if value, err := strconv.Atoi(part); err != nil {
			log.Fatal(err)
		} else {
			values = append(values, value)
		}
	}
	return values
}
