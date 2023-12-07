from functools import cmp_to_key

strengths = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 10,
    "Q": 11,
    "K": 12,
    "A": 13,
}


def hand_type(hand: str) -> int:
    """Determines hand type.

    Parameters
    ----------
    hand : str
        The hand.

    Returns
    -------
    int
        The hand type as a value of 7 to 1 in descending value order.
    """
    counts = {}
    for card in hand:
        if card in counts:
            counts[card] += 1
        else:
            counts[card] = 1
    sorted_counts = sorted([v for _, v in counts.items()], reverse=True)
    if len(sorted_counts) == 1:
        return 7  # Five of a kind
    elif len(sorted_counts) == 2:
        if sorted_counts[0] == 4:
            return 6  # Four of a kind
        else:
            return 5  # Full house
    elif len(sorted_counts) == 3:
        if sorted_counts[0] == 3:
            return 4  # Three of a kind
        else:
            return 3  # Two pairs
    else:
        if sorted_counts[0] == 2:
            return 2  # One pair
        else:
            return 1


def hand_compare(hand1: str, hand2: str) -> int:
    """Compares two hands according to the rules set forth.

    Parameters
    ----------
    hand1 : str
        The first hand.
    hand2 : str
        The second hand.

    Returns
    -------
    int
        +1 if the first hand is greater than the second hand.
        -1 if the first hand is less than the second hand.
        0 if the two hands are equal.
    """
    type1 = hand_type(hand1)
    type2 = hand_type(hand2)
    if type1 > type2:
        return 1
    elif type1 < type2:
        return -1
    else:
        for i in range(5):
            strength1 = strengths[hand1[i]]
            strength2 = strengths[hand2[i]]
            if strength1 > strength2:
                return 1
            elif strength1 < strength2:
                return -1
            else:
                continue
    return 0


def main():
    """Application entry-point."""
    hands: dict[str, int] = {}
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            hand, bid = line.split(" ")
            hands[hand] = int(bid)
    sorted_hands = sorted([hand for hand in hands], key=cmp_to_key(hand_compare))
    total_winnings = 0
    rank = 0
    for hand in sorted_hands:
        rank += 1
        total_winnings += hands[hand] * rank
    print(f"total winnings = {total_winnings}")


if __name__ == "__main__":
    main()
