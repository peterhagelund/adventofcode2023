from re import compile


def process_card(sum: int, index: int, counts: list[int]) -> int:
    """Processes the outcome of a single card.

    Parameters
    ----------
    sum : int
        The current sum.
    index : int
        The current index (not card number).
    counts : list[int]
        The winning card counts.

    Returns
    -------
    int
        The resulting sum.
    """
    sum += 1
    count = counts[index]
    for i in range(1, count + 1):
        new_index = index + i
        if new_index < len(counts):
            sum = process_card(sum, new_index, counts)
    return sum


def main():
    """Application entry-point."""
    pattern = compile(r"\d{1,2}")
    counts = []
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            _, numbers = line[:-1].split(":")
            winning_numbers, my_numbers = numbers.split("|")
            winning_numbers = [int(n) for n in pattern.findall(winning_numbers)]
            my_numbers = [int(n) for n in pattern.findall(my_numbers)]
            count = 0
            for number in my_numbers:
                if number in winning_numbers:
                    count += 1
            counts.append(count)
    sum = 0
    for index in range(len(counts)):
        sum = process_card(sum, index, counts)
    print(f"sum = {sum}")


if __name__ == "__main__":
    main()
