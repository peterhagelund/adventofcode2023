package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

var strengths = map[rune]int{
	'2': 1,
	'3': 2,
	'4': 3,
	'5': 4,
	'6': 5,
	'7': 6,
	'8': 7,
	'9': 8,
	'T': 9,
	'J': 10,
	'Q': 11,
	'K': 12,
	'A': 13,
}

type Hand string
type HandType int

const (
	_ HandType = iota
	HandTypeOther
	HandTypeOnePair
	HandTypeTwoPairs
	HandTypeThreeOfAKind
	HandTypeFullHouse
	HandTypeFourOfAkind
	HandTypeFiveOfAKind
)

func (h Hand) Type() HandType {
	counts := map[rune]int{}
	for _, card := range h {
		count, ok := counts[card]
		if ok {
			count++
		} else {
			count = 1
		}
		counts[card] = count
	}
	sorted_counts := make([]int, 0)
	for _, v := range counts {
		sorted_counts = append(sorted_counts, v)
	}
	sort.Slice(sorted_counts, func(i, j int) bool {
		return sorted_counts[i] > sorted_counts[j]
	})
	switch len(sorted_counts) {
	case 1:
		return HandTypeFiveOfAKind
	case 2:
		if sorted_counts[0] == 4 {
			return HandTypeFourOfAkind
		} else {
			return HandTypeFullHouse
		}
	case 3:
		if sorted_counts[0] == 3 {
			return HandTypeThreeOfAKind
		} else {
			return HandTypeTwoPairs
		}
	default:
		if sorted_counts[0] == 2 {
			return HandTypeOnePair
		} else {
			return HandTypeOther
		}
	}
}

func (h Hand) Less(other Hand) bool {
	type1 := h.Type()
	type2 := other.Type()
	if type1 < type2 {
		return true
	} else if type1 > type2 {
		return false
	} else {
		runes1 := []rune(h)
		runes2 := []rune(other)
		for i := 0; i < 5; i++ {
			if strengths[runes1[i]] < strengths[runes2[i]] {
				return true
			} else if strengths[runes1[i]] > strengths[runes2[i]] {
				return false
			}
		}
	}
	return false
}

func main() {
	file, err := os.Open("puzzle_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	hands := make(map[Hand]int)
	for scanner.Scan() {
		fields := strings.Fields(scanner.Text())
		hand := Hand(fields[0])
		bid, err := strconv.Atoi(fields[1])
		if err != nil {
			log.Fatal(err)
		}
		hands[hand] = bid
	}
	sorted_hands := make([]Hand, 0)
	for k := range hands {
		sorted_hands = append(sorted_hands, k)
	}
	sort.Slice(sorted_hands, func(i, j int) bool {
		return sorted_hands[i].Less(sorted_hands[j])
	})
	total_winnings := 0
	rank := 0
	for _, hand := range sorted_hands {
		rank++
		total_winnings += hands[hand] * rank
	}
	fmt.Printf("total winnings = %d\n", total_winnings)
}
