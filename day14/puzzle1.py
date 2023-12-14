def tilt(platform: list[list[str]]):
    """Tilts the platform by rolling all the round rocks as far "up" as they can go.

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
    tilt(platform)
    load = calculate_load(platform)
    print(f"load = {load}")


if __name__ == "__main__":
    main()
