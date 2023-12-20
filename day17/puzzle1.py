from heapq import heappop, heappush


def determine_heat_loss(grid: list[list[int]]) -> int:
    """Determines the heat loss.

    Parameters
    ----------
    grid : list[list[int]]
        The grid.

    Returns
    -------
    int
        The heat loss.
    """
    height = len(grid)
    width = len(grid[0])
    seen = set()
    queue = [(0, 0, 0, 0, 0, 0)]
    while queue:
        heat_loss, y, x, dy, dx, steps = heappop(queue)
        if y == height - 1 and x == width - 1:
            return heat_loss
        if (y, x, dy, dx, steps) in seen:
            continue
        seen.add((y, x, dy, dx, steps))
        if steps < 3 and (dy, dx) != (0, 0):
            ny = y + dy
            nx = x + dx
            if 0 <= ny < height and 0 <= nx < width:
                heappush(queue, (heat_loss + grid[ny][nx], ny, nx, dy, dx, steps + 1))
        for ndy, ndx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (ndy, ndx) != (dy, dx) and (ndy, ndx) != (-dy, -dx):
                ny = y + ndy
                nx = x + ndx
                if 0 <= ny < height and 0 <= nx < width:
                    heappush(queue, (heat_loss + grid[ny][nx], ny, nx, ndy, ndx, 1))
    return 0


def main():
    grid: list[list[int]] = []
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            grid.append(list(map(int, line.strip())))
    heat_loss = determine_heat_loss(grid)
    print(f"heat loss = {heat_loss}")


if __name__ == "__main__":
    main()
