from collections import deque
from enum import Enum
from os import DirEntry


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
    energized: list[list[bool]] = []
    for row in contraption:
        energized.append([False for _ in row])
    queue = deque([start])
    while queue:
        leg: tuple[int, int, Direction] = queue.popleft()
        if leg in legs:
            continue
        legs.append(leg)
        y = leg[0]
        x = leg[1]
        direction = leg[2]
        while True:
            if contraption[y][x] == ".":
                energized[y][x] = True
                if direction == Direction.RIGHT:
                    x += 1
                    if x == len(contraption[y]):
                        break
                elif direction == Direction.LEFT:
                    x -= 1
                    if x < 0:
                        break
                elif direction == Direction.DOWN:
                    y += 1
                    if y == len(contraption):
                        break
                else:
                    y -= 1
                    if y < 0:
                        break
            elif contraption[y][x] == "|":
                energized[y][x] = True
                if direction == Direction.DOWN:
                    y += 1
                    if y == len(contraption):
                        break
                elif direction == Direction.UP:
                    y -= 1
                    if y == 0:
                        break
                else:
                    if y > 0:
                        queue.append((y - 1, x, Direction.UP))
                    if y < len(contraption) - 1:
                        queue.append((y + 1, x, Direction.DOWN))
                    break
            elif contraption[y][x] == "-":
                energized[y][x] = True
                if direction == Direction.RIGHT:
                    x += 1
                    if x == len(contraption[y]):
                        break
                elif direction == Direction.LEFT:
                    x -= 1
                    if x < 0:
                        break
                else:
                    if x > 0:
                        queue.append((y, x - 1, Direction.LEFT))
                    if x < len(contraption[y]) - 1:
                        queue.append((y, x + 1, Direction.RIGHT))
                    break
            elif contraption[y][x] == "/":
                energized[y][x] = True
                if direction == Direction.RIGHT:
                    if y > 0:
                        queue.append((y - 1, x, Direction.UP))
                elif direction == Direction.LEFT:
                    if y < len(contraption) - 1:
                        queue.append((y + 1, x, Direction.DOWN))
                elif direction == Direction.DOWN:
                    if x > 0:
                        queue.append((y, x - 1, Direction.LEFT))
                else:
                    if x < len(contraption[y]) - 1:
                        queue.append((y, x + 1, Direction.RIGHT))
                break
            elif contraption[y][x] == "\\":
                energized[y][x] = True
                if direction == Direction.RIGHT:
                    if y < len(contraption) - 1:
                        queue.append((y + 1, x, Direction.DOWN))
                elif direction == Direction.LEFT:
                    if y > 0:
                        queue.append((y - 1, x, Direction.UP))
                elif direction == Direction.DOWN:
                    if x < len(contraption[y]) - 1:
                        queue.append((y, x + 1, Direction.RIGHT))
                else:
                    if x > 0:
                        queue.append((y, x - 1, Direction.LEFT))
                break
            else:
                raise ValueError(contraption[y][x])
    tile_count = 0
    for row in energized:
        tile_count += sum([0 if not tile else 1 for tile in row])
    return tile_count


def main():
    """Application entry-point."""
    contraption: list[list[str]] = []
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            contraption.append(list(line.strip()))
    tile_counts: list[int] = []
    for x in range(len(contraption[0])):
        tile_counts.append(calculate_energized_tiles(contraption, (0, x, Direction.DOWN)))
        tile_counts.append(calculate_energized_tiles(contraption, (len(contraption) - 1, x, Direction.UP)))
    for y in range(len(contraption)):
        tile_counts.append(calculate_energized_tiles(contraption, (y, 0, Direction.RIGHT)))
        tile_counts.append(calculate_energized_tiles(contraption, (y, len(contraption[0]) - 1, Direction.LEFT)))
    tile_count = max(tile_counts)
    print(f"energized tiles = {tile_count}")


if __name__ == "__main__":
    main()
