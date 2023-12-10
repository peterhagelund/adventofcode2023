from collections import deque
from typing import Optional


def find_start(maze: list[str]) -> Optional[tuple[int, int]]:
    """Finds the start of the pipe maze.

    Parameters
    ----------
    maze : list[str]
        The maze.

    Returns
    -------
    (int, int)
        The starting point (y, x) or `None`.
    """
    for y in range(len(maze)):
        x = maze[y].find("S")
        if x != -1:
            return (y, x)
    return None


def calculate_outside_count(start: tuple[int, int], maze: list[str]) -> int:
    """Calculates the outside count.

    Determine what pipe-character `S` replaces in order for algorithm to work.
    Initially it can be any of the charcters, but as we see different neighbors (north, south, east, west)
    we can whittle down the options to just one.

    Toggle inside/outside flag on `|` and end-of-runs of `L` to `J`.
    Don't toggle on runs of `F` to `7` because we're running horizontally at the bottom of the line.

    Parameters
    ----------
    start : tuple[int, int]
        The start.
    maze : list[str]
        The maze.

    Returns
    -------
    int
        The count of steps to the farthest point.
    """
    height = len(maze)
    width = len(maze[0])  # We already know all lines are the same length; otherwise this wouldn't work.
    queue = deque([start])
    moves: set[tuple[int, int]] = {start}
    actual_s = {"|", "-", "J", "L", "7", "F"}

    while queue:
        pos = queue.popleft()
        y, x = pos[0], pos[1]
        c = maze[y][x]
        if y > 0 and c in "S|JL" and maze[y - 1][x] in "|7F" and (y - 1, x) not in moves:
            moves.add((y - 1, x))
            queue.append((y - 1, x))
            if c == "S":
                actual_s &= {"|", "J", "L"}
        if y < height - 1 and c in "S|7F" and maze[y + 1][x] in "|JL" and (y + 1) not in moves:
            moves.add((y + 1, x))
            queue.append((y + 1, x))
            if c == "S":
                actual_s &= {"|", "7", "F"}
        if x > 0 and c in "S-J7" and maze[y][x - 1] in "-LF" and (y, x - 1) not in moves:
            moves.add((y, x - 1))
            queue.append((y, x - 1))
            if c == "S":
                actual_s &= {"-", "J", "7"}
        if x < width - 1 and c in "S-LF" and maze[y][x + 1] in "-J7" and (y, x + 1) not in moves:
            moves.add((y, x + 1))
            queue.append((y, x + 1))
            if c == "S":
                actual_s &= {"-", "L", "F"}
    s = actual_s.pop()
    maze = [line.replace("S", s) for line in maze]
    maze = ["".join(c if (y, x) in moves else "." for x, c in enumerate(line)) for y, line in enumerate(maze)]
    outside_tiles: set[tuple[int, int]] = set()
    for y in range(height):
        line = maze[y]
        outside = True
        vertical = False
        for x in range(width):
            c = line[x]
            if c == "|":
                outside = not outside
            elif c == "-":
                pass  # We're going horizontal
            elif c in "LF":
                vertical = c == "L"
            elif c in "7J":
                if c != ("J" if vertical else "7"):  # Toggle at the end of this run (`J` if start was `L`; `7` if start was `F`)
                    outside = not outside
                vertical = False
            elif c == ".":
                pass
            if outside:
                outside_tiles.add((y, x))
    return height * width - len(outside_tiles | moves)


def main():
    """Application entry-point."""
    maze: list[str] = []
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            maze.append(line.strip())
    start = find_start(maze)
    if not start:
        print("No 'S' found")
        return
    print(f"start = {start}")
    count = calculate_outside_count(start, maze)
    print(f"count = {count}")


if __name__ == "__main__":
    main()
