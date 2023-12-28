coordinate = list[int, int, int]
brick = tuple[coordinate, coordinate]

X = 0
Y = 1
Z = 2


def overlaps(b1: brick, b2: brick) -> bool:
    """Determines whether or not there is overlap in the X/Y plan between two bricks.

    Parameters
    ----------
    b1 : brick
        The first brick.
    b2 : brick
        The second brick.

    Returns
    -------
    bool
        `True` if there is overlap; `False` otherwise.
    """
    return max(b1[0][X], b2[0][X]) <= min(b1[1][X], b2[1][X]) and max(b1[0][Y], b2[0][Y]) <= min(b1[1][Y], b2[1][Y])


def drop_bricks(bricks: list[brick]):
    """Drops the bricks.

    Parameters
    ----------
    bricks : list[brick]
        The bricks.
    """
    for i, b1 in enumerate(bricks):
        max_z = 1
        for b2 in bricks[:i]:
            if overlaps(b1, b2):
                max_z = max(max_z, b2[1][Z] + 1)
            b1[1][Z] -= b1[0][Z] - max_z
            b1[0][Z] = max_z
    bricks.sort(key=lambda brick: brick[0][Z])


def determine_supports(bricks: list[brick]) -> tuple[dict[int, set], dict[int, set]]:
    """Determines which bricks support other bricks.

    Parameters
    ----------
    bricks : list[brick]
        The bricks.

    Returns
    -------
    tuple[dict[int, set], dict[int, set]]
        _description_
    """
    does_support = {i: set() for i in range(len(bricks))}
    is_supported_by = {i: set() for i in range(len(bricks))}
    for j, b1 in enumerate(bricks):
        for i, b2 in enumerate(bricks[:j]):
            if overlaps(b1, b2) and b1[0][Z] == b2[1][Z] + 1:
                does_support[i].add(j)
                is_supported_by[j].add(i)
    return (does_support, is_supported_by)


def main():
    """Application entry-point."""
    bricks: list[brick] = []
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            end1, end2 = line.strip().split("~")
            coords1: coordinate = [int(c) for c in end1.split(",")]
            coords2: coordinate = [int(c) for c in end2.split(",")]
            bricks.append((coords1, coords2))
    bricks.sort(key=lambda brick: brick[0][Z])
    drop_bricks(bricks)
    does_support, is_supported_by = determine_supports(bricks)
    total = 0
    for i in range(len(bricks)):
        if all(len(is_supported_by[j]) >= 2 for j in does_support[i]):
            total += 1
    print(f"total = {total}")


if __name__ == "__main__":
    main()
