package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"log"
	"os"
)

type State struct {
	y     int
	x     int
	dy    int
	dx    int
	steps int
}

type Move struct {
	heatLoss int
	state    State
}

type MoveHeap []*Move

func (lh MoveHeap) Len() int {
	return len(lh)
}

func (lh MoveHeap) Less(i, j int) bool {
	return lh[i].heatLoss < lh[j].heatLoss
}

func (lh MoveHeap) Swap(i, j int) {
	lh[i], lh[j] = lh[j], lh[i]
}

func (lh *MoveHeap) Push(x any) {
	leg := x.(*Move)
	*lh = append(*lh, leg)
}

func (lh *MoveHeap) Pop() any {
	old := *lh
	n := len(old)
	leg := old[n-1]
	old[n-1] = nil
	*lh = old[0 : n-1]
	return leg
}

func main() {
	file, err := os.Open("puzzle_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	grid := make([][]int, 0)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		row := make([]int, 0)
		for _, r := range scanner.Text() {
			row = append(row, int(r-'0'))
		}
		grid = append(grid, row)
	}
	heatLoss := determineHeatLoss(grid)
	fmt.Printf("heat loss = %d\n", heatLoss)
}

func determineHeatLoss(grid [][]int) int {
	height := len(grid)
	width := len(grid[0])
	seen := make(map[State]bool)
	queue := make(MoveHeap, 1)
	queue[0] = &Move{0, State{0, 0, 0, 0, 0}}
	heap.Init(&queue)
	for len(queue) > 0 {
		move := heap.Pop(&queue).(*Move)
		state := move.state
		if state.y == height-1 && state.x == width-1 {
			return move.heatLoss
		}
		if _, ok := seen[state]; ok {
			continue
		}
		seen[state] = true
		if state.steps < 3 && !(state.dy == 0 && state.dx == 0) {
			ny := state.y + state.dy
			nx := state.x + state.dx
			if ny >= 0 && ny < height && nx >= 0 && nx < width {
				heap.Push(&queue, &Move{move.heatLoss + grid[ny][nx], State{ny, nx, state.dy, state.dx, state.steps + 1}})
			}
		}
		for _, delta := range [4][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}} {
			ndy := delta[0]
			ndx := delta[1]
			if !(ndy == state.dy && ndx == state.dx) && !(ndy == -state.dy && ndx == -state.dx) {
				ny := state.y + ndy
				nx := state.x + ndx
				if ny >= 0 && ny < height && nx >= 0 && nx < width {
					heap.Push(&queue, &Move{move.heatLoss + grid[ny][nx], State{ny, nx, ndy, ndx, 1}})
				}
			}
		}
	}
	return 0
}
