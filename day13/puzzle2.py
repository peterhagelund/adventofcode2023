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


def fix_smudge(patterns: list[str]) -> int:
    for y in range(len(patterns)):
        for x in range(len(patterns[y])):
            _patterns: list[str] = []
            for _y, r in enumerate(patterns):
                if _y == y:
                    replacement = "#" if r[x] == "." else "."
                    _patterns.append(r[:x] + replacement + r[x + 1 :])
                else:
                    _patterns.append(r)
            result = find_reflection(_patterns)
            if result != 0:
                return result
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
    for x in range(len(patterns[0])):
        r: list[str] = []
        for y in range(len(patterns)):
            r.append(patterns[y][x])
        _patterns.append("".join(r))
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
        The score as 100 * horizontal + vertical - either or both of which could be `0`.
    """
    result = fix_smudge(patterns) * 100
    patterns = flip_patterns(patterns)
    result += fix_smudge(patterns)
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
