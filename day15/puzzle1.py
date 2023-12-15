def hash(value: str) -> int:
    """Calculates the `hash` value of a string.

    For each character in `value` add the ASCII value, multiply by `17` and take remainder of dividing by `256`.

    Parameters
    ----------
    value : str
        The value.

    Returns
    -------
    int
        The `hash`.
    """
    h = 0
    for c in value:
        h += ord(c)
        h *= 17
        h %= 256
    return h


def main():
    """Application entry-point."""
    with open("puzzle_input.txt", "rt") as f:
        input = f.read()
    sum = 0
    steps = input.split(",")
    for step in steps:
        sum += hash(step)
    print(f"sum = {sum}")


if __name__ == "__main__":
    main()
