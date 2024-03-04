package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"slices"
	"strconv"
	"strings"
)

type lens struct {
	label       string
	focalLength int
}

type box struct {
	lenses []*lens
}

func main() {
	file, err := os.Open("puzzle_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	if !scanner.Scan() {
		log.Fatal("can't read")
	}
	boxes := make([]*box, 256)
	for i := 0; i < 256; i++ {
		boxes[i] = &box{
			lenses: make([]*lens, 0),
		}
	}
	focusingPower := 0
	steps := strings.Split(scanner.Text(), ",")
	for _, step := range steps {
		if strings.ContainsRune(step, '-') {
			parts := strings.Split(step, "-")
			doRemove(boxes, parts[0])
		} else {
			parts := strings.Split(step, "=")
			focalLength, err := strconv.Atoi(parts[1])
			if err != nil {
				log.Fatal(err)
			}
			doAdd(boxes, parts[0], focalLength)
		}
	}
	for i, box := range boxes {
		for j, l := range box.lenses {
			focusingPower += (i + 1) * (j + 1) * l.focalLength
		}
	}
	fmt.Printf("focusing power = %d\n", focusingPower)
}

func doRemove(boxes []*box, label string) {
	box := boxes[hash(label)]
	index := slices.IndexFunc(box.lenses, func(l *lens) bool {
		return l.label == label
	})
	if index >= 0 {
		box.lenses = slices.Delete(box.lenses, index, index+1)
	}
}

func doAdd(boxes []*box, label string, focalLength int) {
	box := boxes[hash(label)]
	index := slices.IndexFunc(box.lenses, func(l *lens) bool {
		return l.label == label
	})
	if index >= 0 {
		box.lenses[index].focalLength = focalLength
	} else {
		box.lenses = append(box.lenses, &lens{label, focalLength})
	}
}

func hash(value string) int {
	h := 0
	for _, b := range value {
		h += int(b)
		h *= 17
		h %= 256
	}
	return h
}
