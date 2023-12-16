from collections import deque
from enum import Enum


class Direction(Enum):
    """Possible directions."""

    RIGHT = 1
    DOWN = 2
    LEFT = 3
    UP = 4


def calculate_energized_tiles(contraption: list[list[str]], start: tuple[int, int, Direction]) -> int:
    """Calculates energized tiles.

    Parameters
    ----------
    contraption : list[list[str]]
        The contraption.
    start : tuple[int, int, Direction]
        The starting point.

    Returns
    -------
    int
        The energized tile count.

    Raises
    ------
    ValueError
        If an invalid tile is encountered.
    """
    legs: list[tuple[int, int, Direction]] = []
    energized: list[list[bool]] = [[False for _ in row] for row in contraption]
    queue = deque([start])
    height = len(contraption)
    width = len(contraption[0])
    while queue:
        leg = queue.popleft()
        if leg in legs:
            continue
        legs.append(leg)
        (y, x, direction) = leg
        while True:
            energized[y][x] = True
            tile = contraption[y][x]
            if direction == Direction.RIGHT:
                if tile in ".-":
                    x += 1
                    if x == width:
                        break
                else:
                    if y > 0 and tile in "|/":
                        queue.append((y - 1, x, Direction.UP))
                    if y + 1 < height and tile in "|\\":
                        queue.append((y + 1, x, Direction.DOWN))
                    break
            elif direction == Direction.DOWN:
                if tile in ".|":
                    y += 1
                    if y == height:
                        break
                else:
                    if x > 0 and tile in "-/":
                        queue.append((y, x - 1, Direction.LEFT))
                    if x + 1 < width and tile in "-\\":
                        queue.append((y, x + 1, Direction.RIGHT))
                    break
            elif direction == Direction.LEFT:
                if tile in ".-":
                    x -= 1
                    if x < 0:
                        break
                else:
                    if y > 0 and tile in "|\\":
                        queue.append((y - 1, x, Direction.UP))
                    if y < height - 1 and tile in "|/":
                        queue.append((y + 1, x, Direction.DOWN))
                    break
            else:
                if tile in ".|":
                    y -= 1
                    if y < 0:
                        break
                else:
                    if x > 0 and tile in "-\\":
                        queue.append((y, x - 1, Direction.LEFT))
                    if x + 1 < width and tile in "-/":
                        queue.append((y, x + 1, Direction.RIGHT))
                    break
    return sum([sum([0 if not tile else 1 for tile in row]) for row in energized])


def main():
    """Application entry-point."""
    contraption: list[list[str]] = []
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            contraption.append(list(line.strip()))
    tile_count = 0
    for x in range(len(contraption[0])):
        tile_count = max(tile_count, calculate_energized_tiles(contraption, (0, x, Direction.DOWN)))
        tile_count = max(tile_count, calculate_energized_tiles(contraption, (len(contraption) - 1, x, Direction.UP)))
    for y in range(len(contraption)):
        tile_count = max(tile_count, calculate_energized_tiles(contraption, (y, 0, Direction.RIGHT)))
        tile_count = max(tile_count, calculate_energized_tiles(contraption, (y, len(contraption[0]) - 1, Direction.LEFT)))
    print(f"energized tiles = {tile_count}")


if __name__ == "__main__":
    main()
