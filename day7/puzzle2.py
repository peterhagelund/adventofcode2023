from dataclasses import dataclass
from functools import cmp_to_key

cards = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
strengths = {}
for i in range(len(cards)):
    strengths[cards[i]] = i + 1


@dataclass
class Game:
    """Encapsulation of a single game."""

    original_hand: str
    original_type: int
    upgraded_hand: str
    upgraded_type: int
    bid: int


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
            return 1  # High card


def upgrade_hand(game: Game):
    """Upgrades game to highest possible type.

    Parameters
    ----------
    game : Game
        The game.
    """
    if game.original_type == 7:
        return
    if "J" not in game.original_hand:
        return
    for card in reversed(cards[1:]):
        upgraded_hand = game.original_hand.replace("J", card)
        upgraded_type = hand_type(upgraded_hand)
        if upgraded_type > game.upgraded_type:
            game.upgraded_hand = upgraded_hand
            game.upgraded_type = upgraded_type


def game_compare(game1: Game, game2: Game) -> int:
    """Compares two games according to the rules set forth.

    Parameters
    ----------
    game1 : Game
        The first game.
    game2: Game
        The second game.

    Returns
    -------
    int
        +1 if the first game is greater than the second game.
        -1 if the first game is less than the second game.
        0 if the two games are equal.
    """
    if game1.upgraded_type > game2.upgraded_type:
        return 1
    elif game1.upgraded_type < game2.upgraded_type:
        return -1
    else:
        for i in range(5):
            strength1 = strengths[game1.original_hand[i]]
            strength2 = strengths[game2.original_hand[i]]
            if strength1 > strength2:
                return 1
            elif strength1 < strength2:
                return -1
            else:
                continue
    return 0


def main():
    """Application entry-point."""
    games = []
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            original_hand, bid = line.split(" ")
            original_type = hand_type(original_hand)
            game = Game(original_hand=original_hand, original_type=original_type, upgraded_hand=original_hand, upgraded_type=original_type, bid=int(bid))
            upgrade_hand(game)
            games.append(game)
    total_winnings = 0
    rank = 0
    sorted_games = sorted(games, key=cmp_to_key(game_compare))
    for game in sorted_games:
        rank += 1
        total_winnings += game.bid * rank
    print(f"total winnings = {total_winnings}")


if __name__ == "__main__":
    main()
