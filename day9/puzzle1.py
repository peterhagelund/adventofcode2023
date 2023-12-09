def extrapolate(values: list[int]) -> int:
    """Extrapolates the next value.

    Parameters
    ----------
    values : list[int]
        The values.

    Returns
    -------
    int
        The extrapolated value.
    """
    sequences: list[list[int]] = []
    sequence = values
    while True:
        sequences.append(sequence)
        if min(sequence) == 0 and max(sequence) == 0:
            break
        differences = []
        for i in range(len(sequence) - 1):
            difference = sequence[i + 1] - sequence[i]
            differences.append(difference)
        sequence = differences
    last = 0
    for i in range(len(sequences) - 1, -1, -1):
        sequence = sequences[i]
        if i == len(sequences) - 1:
            sequence.append(last)
        else:
            last = sequence[-1] + last
            sequence.append(last)
    return last


def main():
    """Application entry-point."""
    sum = 0
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            values = [int(value) for value in line.split(" ")]
            sum += extrapolate(values)
    print(f"sum = {sum}")


if __name__ == "__main__":
    main()
