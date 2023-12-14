def tilt_north(platform: list[list[str]]):
    """Tilts the platform north by rolling all the round rocks as far "up" as they can go.

    Parameters
    ----------
    platform : list[list[str]]
        The platform.
    """
    for y in range(1, len(platform)):
        for x in range(len(platform[0])):
            if platform[y][x] != "O":
                continue
            _y = y
            while _y > 0 and platform[_y - 1][x] == ".":
                platform[_y - 1][x] = "O"
                platform[_y][x] = "."
                _y -= 1


def tilt_west(platform: list[list[str]]):
    """Tilts the platform west by rolling all the round rocks as far "left" as they can go.

    Parameters
    ----------
    platform : list[list[str]]
        The platform.
    """
    for x in range(1, len(platform[0])):
        for y in range(len(platform)):
            if platform[y][x] != "O":
                continue
            _x = x
            while _x > 0 and platform[y][_x - 1] == ".":
                platform[y][_x - 1] = "O"
                platform[y][_x] = "."
                _x -= 1


def tilt_south(platform: list[list[str]]):
    """Tilts the platform south by rolling all the round rocks as far "down" as they can go.

    Parameters
    ----------
    platform : list[list[str]]
        The platform.
    """
    for y in range(len(platform) - 2, -1, -1):
        for x in range(len(platform[0])):
            if platform[y][x] != "O":
                continue
            _y = y
            while _y < len(platform) - 1 and platform[_y + 1][x] == ".":
                platform[_y + 1][x] = "O"
                platform[_y][x] = "."
                _y += 1


def tilt_east(platform: list[list[str]]):
    """Tilts the platform east by rolling all the round rocks as far "right" as they can go.

    Parameters
    ----------
    platform : list[list[str]]
        The platform.
    """
    for x in range(len(platform[0]) - 2, -1, -1):
        for y in range(len(platform)):
            if platform[y][x] != "O":
                continue
            _x = x
            while _x < len(platform[0]) - 1 and platform[y][_x + 1] == ".":
                platform[y][_x + 1] = "O"
                platform[y][_x] = "."
                _x += 1


def calculate_load(platform: list[list[str]]) -> int:
    """Calculates the load on the platform.

    Parameters
    ----------
    platform : list[list[str]]
        The platform.

    Returns
    -------
    int
        The load.
    """
    load = 0
    for y in range(len(platform)):
        for x in range(len(platform[y])):
            if platform[y][x] == "O":
                load += len(platform) - y
    return load


def main():
    """Application entry-point."""
    platform: list[list[str]] = []
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            platform.append(list(line.strip()))
    loads: list[int] = []
    unique: set[int] = set()
    # Keep tilting until no new loads have been created...
    while True:
        for f in [tilt_north, tilt_west, tilt_south, tilt_east]:
            f(platform)
        load = calculate_load(platform)
        loads.append(load)
        unique.add(load)
        if len(unique) < len(loads):
            break
    repeat = loads[-1]
    print(f"first repeat is {repeat}")
    index = loads.index(repeat)
    print(f"index = {index}")
    cycle = len(loads) - index - 1
    print(f"cycle = {cycle}")
    offset = (999999999 - index) % cycle
    print(f"offset = {offset}")
    print(f"load = {loads[index + offset]}")


if __name__ == "__main__":
    main()
