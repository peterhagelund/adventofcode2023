from re import compile


def find_arrangements(conditions: str, sizes: list[int]) -> int:
    """Finds all possible arrangement of the conditions that fit the `list` of sizes.

    By looking at the problem as a binary number, the number of permutations is 2 ** (number of "?").
    Then looping through the number of permutations, a binary `0` equals a `.` and a binary `1` equals a `#`.
    Then, using regex with the pattern `r"#+"` we find all the runs of `#` and a simple `list` equality comparison
    determines if the permutation is a match for the arrangement or not.

    Parameters
    ----------
    conditions : str
        The conditions.
    sizes : list[int]
        The sizes from the records.

    Returns
    -------
    int
        The number of possible arrangements.
    """
    count = 2 ** conditions.count("?")
    arrangements = 0
    pattern = compile(r"#+")
    for p in range(count):
        _conditions: list[str] = []
        _p = 0
        for i in range(len(conditions)):
            c = conditions[i]
            if c == "?":
                if p & (1 << _p) == 0:
                    c = "."
                else:
                    c = "#"
                _p += 1
            _conditions.append(c)
        _conditions = "".join(_conditions)
        _sizes = [len(run) for run in pattern.findall(_conditions)]
        if _sizes == sizes:
            arrangements += 1
    return arrangements


def main():
    """Application entry-point."""
    records: list[tuple[str, list[int]]] = []
    with open("test_input.txt", "rt") as f:
        for line in f:
            conditions, sizes = line.strip().split(" ")
            sizes = [int(size) for size in sizes.split(",")]
            records.append((conditions, sizes))
    sum = 0
    for row in records:
        sum += find_arrangements(row[0], row[1])
    print(f"sum = {sum}")


if __name__ == "__main__":
    main()
