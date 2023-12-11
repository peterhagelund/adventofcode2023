def expand_space(space: list[str]):
    """Expands space by doubling rows and columns entirely made up of `.` characters.

    Parameters
    ----------
    space : list[str]
        The space.
    """
    height = len(space)
    width = len(space[0])
    y = 0
    while y < height:
        if space[y].count(".") == width:
            space.insert(y, "." * width)
            y += 1
            height += 1
        y += 1
    x = 0
    while x < width:
        count = 0
        for y in range(height):
            if space[y][x] == ".":
                count += 1
        if count == height:
            for y in range(height):
                space[y] = space[y][:x] + "." + space[y][x:]
            x += 1
            width += 1
        x += 1


def build_galaxy_map(space: list[str]) -> dict[int, tuple[int, int]]:
    """Builds the galaxy map.

    Parameters
    ----------
    space : list[str]
        The space.

    Returns
    -------
    dict[int, tuple[int, int]]
        The galaxy map.
    """
    map: dict[int, tuple[int, int]] = {}
    num = 0
    for y, line in enumerate(space):
        for x in range(len(line)):
            if space[y][x] == "#":
                map[num] = (y, x)
                num += 1
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
    with open("sample_input.txt", "rt") as f:
        for line in f:
            space.append(line.strip())
    expand_space(space)
    map = build_galaxy_map(space)
    pairs = build_galaxy_pairs(len(map))
    sum = 0
    for pair in pairs:
        sum += calculate_distance(map, pair)
    print(f"sum = {sum}")


if __name__ == "__main__":
    main()
