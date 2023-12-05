def source_to_dest(source: int, map: list[tuple[int, int, int]]) -> int:
    """Maps a source to a destination.

    Parameters
    ----------
    source : int
        The source.
    map : list[tuple[int, int, int]]
        The map to use for the mapping operation.

    Returns
    -------
    int
        The destination.
    """
    for r in map:
        if source >= r[1] and source < r[1] + r[2]:
            return r[0] + (source - r[1])
    return source


def main():
    """Application entry-point."""
    with open("puzzle_input.txt", "rt") as f:
        seeds: list[int] = None
        maps: list[list[tuple[int, int, int]]] = []
        map_index = -1
        for line in f:
            line = line.strip()
            if len(line) == 0:
                continue
            if line.startswith("seeds: "):
                seeds = [int(seed) for seed in line[7:].split(" ")]
            elif line.endswith(" map:"):
                map_index += 1
                maps.append([])
            else:
                values = [int(v) for v in line.split(" ")]
                maps[map_index].append((values[0], values[1], values[2]))
    locations: list[tuple[int, int]] = []
    for seed in seeds:
        source = seed
        for map_index in range(len(maps)):
            dest = source_to_dest(source, maps[map_index])
            source = dest
        location = dest
        locations.append((seed, location))
    locations = sorted(locations, key=lambda t: t[1])
    print(f"lowest location is {locations[0][1]} for seed {locations[0][0]}")


if __name__ == "__main__":
    main()
