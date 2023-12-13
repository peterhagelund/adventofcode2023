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
        size = min(row, len(patterns) - row)
        above = patterns[row - size : row]
        below = [r for r in reversed(patterns[row : row + size])]
        if above == below:
            return row
    return 0


def flip_patterns(patterns: list[str]) -> list[str]:
    """Flips a pattern.

    Parameters
    ----------
    patterns : list[str]
        The patterns.

    Returns
    -------
    list[str]
        The flipped pattern.
    """
    _patterns: list[str] = []
    for c in range(len(patterns[0])):
        _row: list[str] = []
        for r in range(len(patterns)):
            _row.append(patterns[r][c])
        _patterns.append("".join(_row))
    return _patterns


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
    result = find_reflection(patterns) * 100
    patterns = flip_patterns(patterns)
    result += find_reflection(patterns)
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
