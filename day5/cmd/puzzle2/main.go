package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type SeedRange struct {
	Start  int
	Length int
}

type MapEntry struct {
	DestinationStart int
	SourceStart      int
	Length           int
}

type Map struct {
	Name       string
	MapEntries []*MapEntry
}

func NewSeedRange(start int, length int) *SeedRange {
	return &SeedRange{
		Start:  start,
		Length: length,
	}
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

func (s *SeedRange) Contains(seed int) bool {
	return seed >= s.Start && seed < s.Start+s.Length
}

func (m *Map) DestToSource(dest int) int {
	for _, mapEntry := range m.MapEntries {
		if dest >= mapEntry.DestinationStart && dest < mapEntry.DestinationStart+mapEntry.Length {
			return mapEntry.SourceStart + (dest - mapEntry.DestinationStart)
		}
	}
	return dest
}

func main() {
	file, err := os.Open("puzzle_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	seedRanges := make([]*SeedRange, 0)
	maps := make([]*Map, 0)
	var currentMap *Map
	for scanner.Scan() {
		text := scanner.Text()
		if len(text) == 0 {
			continue
		}
		parts := strings.Split(text, ":")
		if strings.HasSuffix(parts[0], "seeds") {
			seeds := numbers(strings.Trim(parts[1], " "))
			for i := 0; i < len(seeds)/2; i++ {
				seedRange := NewSeedRange(seeds[2*i], seeds[2*i+1])
				seedRanges = append(seedRanges, seedRange)
			}
		} else if strings.HasSuffix(parts[0], "map") {
			name := parts[0][:len(parts[0])-4]
			currentMap = NewMap(name)
			maps = append(maps, currentMap)
		} else {
			mapEntry := NewMapEntry(parts[0])
			currentMap.MapEntries = append(currentMap.MapEntries, mapEntry)
		}
	}
	location := -1
	found := false
	for !found {
		location++
		dest := location
		for i := len(maps) - 1; i >= 0; i-- {
			dest = maps[i].DestToSource(dest)
		}
		for _, seedRange := range seedRanges {
			if seedRange.Contains(dest) {
				fmt.Printf("location = %d\n", location)
				found = true
			}
		}
	}
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
