def depth_first_search(tile: tuple[int, int], end: tuple[int, int], graph: dict, seen: set[tuple[int, int]]) -> int:
    """Conducts a depth-first search.

    Parameters
    ----------
    tile : tuple[int, int]
        The tile.
    end : tuple[int, int]
        The end of the path.
    graph : dict
        The graph/
    seen : set[tuple[int, int]]
        The `set` of seen tiles.

    Returns
    -------
    int
        The max length.
    """
    if tile == end:
        return 0
    max_length = -1
    seen.add(tile)
    for t in graph[tile]:
        if t not in seen:
            max_length = max(max_length, depth_first_search(t, end, graph, seen) + graph[tile][t])
    seen.remove(tile)
    return max_length


def build_path_graph(island: list[str], branch_points: list[tuple[int, int]]) -> dict[tuple[int, int] : dict[tuple[int, int], int]]:
    """Builds the path graph.

    Parameters
    ----------
    island : list[str]
        The island.

    branch_points : list[tuple[int, int]]
        The branch points.

    Returns
    -------
    _type_
        _description_
    """
    height = len(island)
    width = len(island[0])
    graph: dict[tuple[int, int] : dict[tuple[int, int], int]] = {tile: {} for tile in branch_points}
    directions = {
        "^": [(-1, 0)],
        "v": [(1, 0)],
        "<": [(0, -1)],
        ">": [(0, 1)],
        ".": [(-1, 0), (1, 0), (0, -1), (0, 1)],
    }
    for start_y, start_x in branch_points:
        stack: list[tuple[int, int, int]] = [(0, start_y, start_x)]
        seen: set[tuple[int, int]] = {(start_y, start_x)}
        while stack:
            n, y, x = stack.pop()
            if n != 0 and (y, x) in branch_points:
                graph[(start_y, start_x)][(y, x)] = n
                continue
            for delta_y, delta_x in directions[island[y][x]]:
                next_y = y + delta_y
                next_x = x + delta_x
                if 0 <= next_y < height and 0 <= next_x < width and island[next_y][next_x] != "#" and (next_y, next_x) not in seen:
                    stack.append((n + 1, next_y, next_x))
                    seen.add((next_y, next_x))
    return graph


def find_branch_points(island: list[str], start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    """Finds the island's branch points.

    Parameters
    ----------
    island : list[str]
        The island.
    start : tuple[int, int]
        The start.
    end : tuple[int, int]
        The end.

    Returns
    -------
    list[tuple[int, int]]
        The branch points.
    """
    branch_points: list[tuple[int, int]] = [start, end]
    for y, row in enumerate(island):
        for x, c in enumerate(row):
            if c == "#":
                continue
            neighbors = 0
            for next_y, new_x in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
                if 0 <= next_y < len(island) and 0 <= new_x < len(island[0]) and island[next_y][new_x] != "#":
                    neighbors += 1
            if neighbors >= 3:
                branch_points.append((y, x))
    return branch_points


def main():
    """Application entry-point."""
    island: list[str] = []
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            island.append(line.strip())
    start = (0, island[0].index("."))
    end = (len(island) - 1, island[-1].index("."))
    branch_points: list[tuple[int, int]] = find_branch_points(island, start, end)
    graph: dict[tuple[int, int] : dict[tuple[int, int], int]] = build_path_graph(island, branch_points)
    seen: set[tuple[int, int]] = set()
    max_length = depth_first_search(start, end, graph, seen)
    print(f"max_length = {max_length}")


if __name__ == "__main__":
    main()
