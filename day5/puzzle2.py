def dest_to_source(dest: int, map: list[tuple[int, int, int]]) -> int:
    for r in map:
        if dest >= r[0] and dest < r[0] + r[2]:
            return r[1] + (dest - r[0])
    return dest


def main():
    """Application entry-point."""
    with open("puzzle_input.txt", "rt") as f:
        seed_ranges: list[tuple[int, int]] = []
        maps: list[list[tuple[int, int, int]]] = []
        map_index = -1
        for line in f:
            line = line.strip()
            if len(line) == 0:
                continue
            if line.startswith("seeds: "):
                values = [int(seed) for seed in line[7:].split(" ")]
                for i in range(int(len(values) / 2)):
                    seed_ranges.append((values[2 * i], values[2 * i + 1]))
            else:
                if line.endswith(" map:"):
                    map_index += 1
                    maps.append([])
                else:
                    values = [int(v) for v in line.split(" ")]
                    maps[map_index].append((values[0], values[1], values[2]))
    location = -1
    found = False
    while not found:
        location += 1
        dest = location
        for map_index in range(6, -1, -1):
            dest = dest_to_source(dest, maps[map_index])
        for seed_range in seed_ranges:
            if dest >= seed_range[0] and dest < seed_range[0] + seed_range[1]:
                print(f"seed = {dest}, location = {location}")
                found = True
                break


if __name__ == "__main__":
    main()
