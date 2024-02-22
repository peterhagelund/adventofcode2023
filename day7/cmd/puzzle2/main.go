package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"slices"
	"sort"
	"strconv"
	"strings"
)

var cards = []rune{'J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A'}
var strengths = map[rune]int{}

type Hand string

type HandType int

type Game struct {
	OriginalHand Hand
	OriginalType HandType
	UpgradedHand Hand
	UpgradedType HandType
	Bid          int
}

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

func (g *Game) Upgrade() {
	if g.OriginalType == HandTypeFiveOfAKind {
		return
	}
	if !strings.ContainsRune(string(g.OriginalHand), 'J') {
		return
	}
	for i := len(cards) - 1; i > 0; i-- {
		upgradedHand := Hand(strings.Map(func(r rune) rune {
			if r == 'J' {
				return cards[i]
			} else {
				return r
			}
		}, string(g.OriginalHand)))
		upgradedType := upgradedHand.Type()
		if upgradedType > g.UpgradedType {
			g.UpgradedHand = upgradedHand
			g.UpgradedType = upgradedType
		}
	}
}

func (g *Game) Compare(other *Game) int {
	type1 := g.UpgradedType
	type2 := other.UpgradedType
	if type1 > type2 {
		return 1
	} else if type1 < type2 {
		return -1
	} else {
		runes1 := []rune(g.OriginalHand)
		runes2 := []rune(other.OriginalHand)
		for i := 0; i < 5; i++ {
			if strengths[runes1[i]] > strengths[runes2[i]] {
				return 1
			} else if strengths[runes1[i]] < strengths[runes2[i]] {
				return -1
			}
		}
	}
	return 0
}

func main() {
	file, err := os.Open("puzzle_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	for i, card := range cards {
		strengths[card] = i + 1
	}
	games := make([]*Game, 0)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		fields := strings.Fields(scanner.Text())
		originalHand := Hand(fields[0])
		originalType := originalHand.Type()
		bid, err := strconv.Atoi(fields[1])
		if err != nil {
			log.Fatal(err)
		}
		game := &Game{
			OriginalHand: originalHand,
			OriginalType: originalType,
			UpgradedHand: originalHand,
			UpgradedType: originalType,
			Bid:          bid,
		}
		game.Upgrade()
		games = append(games, game)
	}
	slices.SortFunc(games, func(g1, g2 *Game) int {
		return g1.Compare(g2)
	})
	total_winnings := 0
	rank := 0
	for _, game := range games {
		rank++
		total_winnings += game.Bid * rank
	}
	fmt.Printf("total winnings = %d\n", total_winnings)

}
