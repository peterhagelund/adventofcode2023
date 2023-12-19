from collections import deque


def determine_lagoon_dimensions(plan: list[tuple[str, int, str]]) -> tuple[int, int, int, int]:
    """Determines the lagoon dimensions.

    Parameters
    ----------
    plan : list[tuple[str, int, str]]
        The plan.

    Returns
    -------
    tuple[int, int, int, int]
        The lagoon width and height and the y, x coordinates of the starting position.
    """
    y, x = 0, 0
    min_x, max_x = x, x
    min_y, max_y = y, y
    for direction, distance, _ in plan:
        if direction == "R":
            for _ in range(distance):
                x += 1
        elif direction == "D":
            for _ in range(distance):
                y += 1
        elif direction == "L":
            for _ in range(distance):
                x -= 1
        elif direction == "U":
            for _ in range(distance):
                y -= 1
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    height = (max_y - min_y) + 1
    width = (max_x - min_x) + 1
    y, x = 0 - min_y, 0 - min_x
    return (height, width, y, x)


def populate_lagoon(lagoon: list[list[str]], plan: list[tuple[str, int, str]], y: int, x: int):
    """Populates the lagoon trench.

    Parameters
    ----------
    lagoon : list[list[str]]
        The lagoon.
    plan : list[tuple[str, int, str]]
        The plan.
    y : int
        Starting y.
    x : int
        Starting x.
    """
    prev = " "
    for direction, distance, _ in plan:
        if direction == "R":
            for i in range(distance):
                if i == 0:
                    lagoon[y][x] = "L" if prev == "D" else "F"
                else:
                    lagoon[y][x] = "-"
                x += 1
        elif direction == "D":
            for i in range(distance):
                if i == 0:
                    lagoon[y][x] = "7" if prev == "R" else "F"
                else:
                    lagoon[y][x] = "|"
                y += 1
        elif direction == "L":
            for i in range(distance):
                if i == 0:
                    lagoon[y][x] = "7" if prev == "U" else "J"
                else:
                    lagoon[y][x] = "-"
                x -= 1
        elif direction == "U":
            for i in range(distance):
                if i == 0:
                    lagoon[y][x] = "J" if prev == "R" else "L"
                else:
                    lagoon[y][x] = "|"
                y -= 1
        prev = direction


def determine_moves(lagoon: list[list[str]], y: int, x: int) -> set[tuple[int, int]]:
    """Determines the trench moves.

    Parameters
    ----------
    lagoon : list[list[str]]
        The lagoon.
    y : int
        The start y.
    x : int
        The start x.

    Returns
    -------
    set[tuple[int, int]]
        The moves.
    """
    lagoon[y][x] = "S"
    start = (y, x)
    height = len(lagoon)
    width = len(lagoon[0])
    queue = deque([start])
    moves: set[tuple[int, int]] = {start}
    actual_s = {"|", "-", "J", "L", "7", "F"}
    while queue:
        pos = queue.popleft()
        y, x = pos[0], pos[1]
        c = lagoon[y][x]
        if y > 0 and c in "S|JL" and lagoon[y - 1][x] in "|7F" and (y - 1, x) not in moves:
            moves.add((y - 1, x))
            queue.append((y - 1, x))
            if c == "S":
                actual_s &= {"|", "J", "L"}
        if y < height - 1 and c in "S|7F" and lagoon[y + 1][x] in "|JL" and (y + 1) not in moves:
            moves.add((y + 1, x))
            queue.append((y + 1, x))
            if c == "S":
                actual_s &= {"|", "7", "F"}
        if x > 0 and c in "S-J7" and lagoon[y][x - 1] in "-LF" and (y, x - 1) not in moves:
            moves.add((y, x - 1))
            queue.append((y, x - 1))
            if c == "S":
                actual_s &= {"-", "J", "7"}
        if x < width - 1 and c in "S-LF" and lagoon[y][x + 1] in "-J7" and (y, x + 1) not in moves:
            moves.add((y, x + 1))
            queue.append((y, x + 1))
            if c == "S":
                actual_s &= {"-", "L", "F"}
    s = actual_s.pop()
    y, x = start
    lagoon[y][x] = s
    return moves


def determine_inside_tiles(lagoon: list[list[str]]) -> set[tuple[int, int]]:
    """Determines the inside tiles.

    Parameters
    ----------
    lagoon : list[list[str]]
        The lagoon.

    Returns
    -------
    set[tuple[int, int]]
        The inside tiles.
    """
    height = len(lagoon)
    width = len(lagoon[0])
    inside_tiles: set[tuple[int, int]] = set()
    for y in range(height):
        line = lagoon[y]
        inside = False
        vertical = False
        for x in range(width):
            c = line[x]
            if c == "|":
                inside = not inside
            elif c == "-":
                pass  # We're going horizontal
            elif c in "LF":
                vertical = c == "L"
            elif c in "7J":
                if c != ("J" if vertical else "7"):  # Toggle at the end of this run (`J` if start was `L`; `7` if start was `F`)
                    inside = not inside
                vertical = False
            elif c == ".":
                pass
            if inside:
                inside_tiles.add((y, x))
    return inside_tiles


def main():
    """Application entry-point."""
    plan: list[tuple[str, int, str]] = []
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            direction, distance, color = line.split()
            plan.append((direction, int(distance), color))
    height, width, y, x = determine_lagoon_dimensions(plan)
    lagoon: list[list[str]] = [["." for _ in range(width)] for _ in range(height)]
    populate_lagoon(lagoon, plan, y, x)
    moves = determine_moves(lagoon, y, x)
    inside_tiles = determine_inside_tiles(lagoon)
    print(f"cubic meters = {len(inside_tiles | moves)}")


if __name__ == "__main__":
    main()
