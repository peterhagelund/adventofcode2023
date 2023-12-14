def find_reflection(patterns: list[str]) -> int:
    """Finds a reflection.

    Parameters
    ----------
    patterns : list[str]
        The patterns.

    Returns
    -------
    int
        The row of the reflection if found; `0` otherwise.
    """
    for row in range(1, len(patterns)):
        above = patterns[:row][::-1]
        below = patterns[row:]
        above = above[: len(below)]
        below = below[: len(above)]
        if above == below:
            return row
    return 0


def process_patterns(patterns: list[str]) -> int:
    """Processes the patterns.

    Parameters
    ----------
    patterns : list[str]
        The patterns.

    Returns
    -------
    int
        The score as 100 * horizontal or vertical.
    """
    result = 0
    result += find_reflection(patterns) * 100
    result += find_reflection(list(zip(*patterns)))
    return result


def main():
    """Application entry-point."""
    patterns: list[str] = []
    sum = 0
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            line = line.strip()
            if len(line) > 0:
                patterns.append(line)
            else:
                sum += process_patterns(patterns)
                patterns.clear()
    if len(patterns) > 0:
        sum += process_patterns(patterns)
    print(f"sum = {sum}")


if __name__ == "__main__":
    main()
