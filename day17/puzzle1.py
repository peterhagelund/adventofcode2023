from collections import deque
from enum import Enum


class Direction(Enum):
    """Possible directions."""

    RIGHT = 1
    DOWN = 2
    LEFT = 3
    UP = 4


def minimize_heat_loss(city: list[list[str]]) -> int:
    height = len(city)
    width = len(city[0])
    queue = deque([(0, 0, direction) for direction in [Direction.RIGHT, Direction.DOWN]])
    while queue:
        (y, x, direction) = queue.popleft()
    return 0


def main():
    """Application entry-point."""
    city: list[list[str]] = []
    with open("sample_input.txt", "rt") as f:
        for line in f:
            city.append(list(line.strip()))
    heat_loss = 0
    print(f"heat loss = {heat_loss}")


if __name__ == "__main__":
    main()
