from re import compile


def process_card(sum: int, index: int, cards: list[tuple[list[int], list[int]]]) -> int:
    """Processes a single

    Parameters
    ----------
    sum : int
        The current sum.
    index : int
        The current card (index, not card number).
    cards : list[tuple[list[int], list[int]]]
        The cards.

    Returns
    -------
    int
        The resulting sum.
    """
    sum += 1
    card = cards[index]
    winning_numbers = card[0]
    my_numbers = card[1]
    count = 0
    for number in my_numbers:
        if number in winning_numbers:
            count += 1
    for i in range(1, count + 1):
        new_index = index + i
        if new_index < len(cards):
            sum = process_card(sum, new_index, cards)
    return sum


def main():
    """Application entry-point."""
    pattern = compile(r"\d{1,2}")
    cards = []
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            _, numbers = line[:-1].split(":")
            winning_numbers, my_numbers = numbers.split("|")
            winning_numbers = [int(n) for n in pattern.findall(winning_numbers)]
            my_numbers = [int(n) for n in pattern.findall(my_numbers)]
            cards.append((winning_numbers, my_numbers))
    sum = 0
    for index in range(len(cards)):
        sum = process_card(sum, index, cards)
    print(f"sum = {sum}")


if __name__ == "__main__":
    main()
