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


def find_farthest_point(start: tuple[int, int], maze: list[str]) -> int:
    """Finds the farthest point away from the `start`.

    Parameters
    ----------
    start : tuple[int, int]
        The start.
    maze : list[str]
        Teh maze.

    Returns
    -------
    int
        The count of steps to the farthest point.
    """
    height = len(maze)
    width = len(maze[0])
    queue = deque([start])
    moves: set[tuple[int, int]] = {start}

    while queue:
        pos = queue.popleft()
        y, x = pos[0], pos[1]
        c = maze[y][x]
        if y > 0 and c in "S|JL" and maze[y - 1][x] in "|7F" and (y - 1, x) not in moves:
            moves.add((y - 1, x))
            queue.append((y - 1, x))
        if y < height - 1 and c in "S|7F" and maze[y + 1][x] in "|JL" and (y + 1) not in moves:
            moves.add((y + 1, x))
            queue.append((y + 1, x))
        if x > 0 and c in "S-J7" and maze[y][x - 1] in "-LF" and (y, x - 1) not in moves:
            moves.add((y, x - 1))
            queue.append((y, x - 1))
        if x < width - 1 and c in "S-LF" and maze[y][x + 1] in "-J7" and (y, x + 1) not in moves:
            moves.add((y, x + 1))
            queue.append((y, x + 1))
    return len(moves) // 2


def main():
    """Application entry-point."""
    maze: list[str] = []
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            maze.append(line.strip())
    for line in maze:
        print(line)
    start = find_start(maze)
    if not start:
        print("No 'S' found")
        return
    print(f"start = {start}")
    count = find_farthest_point(start, maze)
    print(f"count = {count}")


if __name__ == "__main__":
    main()
