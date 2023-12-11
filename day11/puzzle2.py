def get_space_expansion(space: list[str]) -> (list[int], list[int]):
    """Determines the space expansion.

    Parameters
    ----------
    space : list[str]
        The space.

    Returns
    -------
    tuple[list[int], list[int]]
        Tuple of two lists. One containg the `rows` that are expanded and one cotaining the `columns` that are expanded.
    """
    height = len(space)
    width = len(space[0])
    rows: list[int] = []
    columns: list[int] = []
    for y in range(height):
        if space[y].count(".") == width:
            rows.append(y)
    for x in range(width):
        count = 0
        for y in range(height):
            if space[y][x] == ".":
                count += 1
        if count == height:
            columns.append(x)
    return (rows, columns)


def build_galaxy_map(space: list[str], expansion: tuple[list[int], list[int]], factor: int) -> dict[int, tuple[int, int]]:
    """Builds the galaxy map.

    In order to support large expansion factors, such as 1,000,000, this solution does not actually
    alter the `space` structure. Rather, this function keeps the actual `y`, `x` coordinates as well
    as the expanded `_y`, _x`. I.e., we iterate through the original `space` but add map coordinates
    using the expanded values.

    Parameters
    ----------
    space : list[str]
        The space.
    expansion: tuple[list[int], list[int]]
        The tuple of expansion rows and columns.
    factor: int
        The expansion factor.

    Returns
    -------
    dict[int, tuple[int, int]]
        The galaxy map.
    """
    map: dict[int, tuple[int, int]] = {}
    rows = expansion[0]
    columns = expansion[1]
    y = 0
    x = 0
    num = 0
    _y = 0
    for y, line in enumerate(space):
        if y in rows:
            _y += factor
        else:
            _x = 0
            for x in range(len(line)):
                if x in columns:
                    _x += factor
                else:
                    if space[y][x] == "#":
                        map[num] = (_y, _x)
                        num += 1
                    _x += 1
            _y += 1
    return map


def build_galaxy_pairs(count: int) -> list[tuple[int, int]]:
    """Builds the pairs of galaxies.

    Parameters
    ----------
    count : int
        The number of galaxies in the map.

    Returns
    -------
    list[tuple[int, int]]
        The pairs.
    """
    pairs: list[tuple[int, int]] = []
    for g1 in range(count):
        for g2 in range(g1 + 1, count):
            pairs.append((g1, g2))
    return pairs


def calculate_distance(map: dict[int, tuple[int, int]], pair: tuple[int, int]) -> int:
    """Calculates the distance between two galaxies.

    Parameters
    ----------
    map : dict[int, tuple[int, int]]
        The map of galaxies.
    pair : tuple[int, int]
        The pair of galaxies.

    Returns
    -------
    int
        The distance.
    """
    pos0 = map[pair[0]]
    pos1 = map[pair[1]]
    return abs(pos0[0] - pos1[0]) + abs(pos0[1] - pos1[1])


def main():
    """Application entry-point."""
    space: list[str] = []
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            space.append(line.strip())
    expansion = get_space_expansion(space)
    map = build_galaxy_map(space, expansion, factor=1000000)
    pairs = build_galaxy_pairs(len(map))
    sum = 0
    for pair in pairs:
        distance = calculate_distance(map, pair)
        sum += distance
    print(f"sum = {sum}")


if __name__ == "__main__":
    main()
