from collections import deque


def find_start(garden: list[str]) -> tuple[int, int]:
    """Finds the starting position/

    Parameters
    ----------
    garden : list[str]
        The garden.

    Returns
    -------
    tuple[int, int]
        The starting position.
    """
    for y in range(len(garden)):
        for x in range(len(garden[y])):
            if garden[y][x] == "S":
                return (y, x)
    return None


def main():
    """Application entry-point."""
    garden: list[str] = []
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            garden.append(list(line.strip()))
    y, x = find_start(garden)
    height = len(garden)
    width = len(garden[0])
    queue = deque([(y, x, 64)])
    seen: set[tuple[int, int]] = {(y, x)}
    plots: set[tuple[int, int]] = set()
    while queue:
        (y, x, steps) = queue.popleft()
        if steps % 2 == 0:
            plots.add((y, x))
        if steps == 0:
            continue
        if y > 0 and garden[y - 1][x] != "#" and (y - 1, x) not in seen:
            queue.append((y - 1, x, steps - 1))
            seen.add((y - 1, x))
        if x > 0 and garden[y][x - 1] != "#" and (y, x - 1) not in seen:
            queue.append((y, x - 1, steps - 1))
            seen.add((y, x - 1))
        if y + 1 < height and garden[y + 1][x] != "#" and (y + 1, x) not in seen:
            queue.append((y + 1, x, steps - 1))
            seen.add((y + 1, x))
        if x + 1 < width and garden[y][x + 1] != "#" and (y, x + 1) not in seen:
            queue.append((y, x + 1, steps - 1))
            seen.add((y, x + 1))
    print(f"plots = {len(plots)}")


if __name__ == "__main__":
    main()
