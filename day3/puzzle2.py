from re import Match, compile
from sys import argv
from typing import Optional


def load_schematic(file_name: str) -> list[str]:
    """Loads the schematic.

    Parameters
    ----------
    file_name : str
        Name of the file containing the schematic.

    Returns
    -------
    list[str]
        The schematic.
    """
    schematic = []
    with open(file_name, "rt") as f:
        for line in f:
            schematic.append(line[:-1])
    return schematic


def find_numbers(schematic: list[str]) -> list[list[Match]]:
    """Finds all numbers.

    Parameters
    ----------
    schematic : list[str]
        The schematic.

    Returns
    -------
    list[list[Match]]
        The `Match`es containing the numbers.
    """
    numbers = []
    pattern = compile(r"[0-9]{1,3}")
    for line in schematic:
        matches = []
        for match in pattern.finditer(line):
            matches.append(match)
        numbers.append(matches)
    return numbers


def find_adjacent_at_end(matches: list[Match], end: int) -> Optional[Match]:
    """Finds a match for a number whose end is exactly `end`.

    Example
    -------

              1111111111
    01234567890123456789

    ...999*...

    If `*` is found at index `6`, and a number match with `end=6`, it will be returned.

    Parameters
    ----------
    matches : list[Match]
        The matches.
    end : int
        The end.

    Returns
    -------
    Optional[Match]
        The match if found; `None` otherwise.
    """
    for match in matches:
        if match.end() == end:
            return match
    return None


def find_adjacent_at_start(matches: list[Match], start: int) -> Optional[Match]:
    """Finds a match for a number whose start is exactly `start`.

    Example
    -------

              1111111111
    01234567890123456789

    ...*999...

    If `*` is found at index `3`, and a number match with `start=4` it will be returned.

    Parameters
    ----------
    matches : list[Match]
        The matches.
    end : int
        The end.

    Returns
    -------
    Optional[Match]
        The match if found; `None` otherwise.
    """
    for match in matches:
        if match.start() == start:
            return match
    return None


def find_adjacents_near(matches: list[Match], index: int) -> list[Match]:
    """Finds zero, one or two matches for numbers near `*` at `index`.

    Examples
    --------

              1111111111
    01234567890123456789
             999
            *

              1111111111
    01234567890123456789
          999
            *

              1111111111
    01234567890123456789
             999
            *

    Parameters
    ----------
    matches : list[Match]
        The matches.
    index : int
        The index of `*` in the line (above or below).

    Returns
    -------
    list[Match]
        The matches.
    """
    adjacents = []
    for match in matches:
        if match.end() == index or match.start() - 1 == index or (match.start() <= index and match.end() > index):
            adjacents.append(match)
    return adjacents


def find_adjacents(numbers: list[list[Match]], line_no: int, index: int) -> list[Match]:
    """Find numbers adjacent to a `*`.

    Parameters
    ----------
    numbers : list[list[Match]]
        The numbers.
    line_no : int
        The line number where the `*` is found.
    index : int
        The index in the line where the `*` is found.

    Returns
    -------
    list[Match]
        The adjacents.
    """
    adjacents = []
    adjacent = find_adjacent_at_end(numbers[line_no], index)
    if adjacent:
        adjacents.append(adjacent)
    adjacent = find_adjacent_at_start(numbers[line_no], index + 1)
    if adjacent:
        adjacents.append(adjacent)
    if line_no > 0:
        adjacents += find_adjacents_near(numbers[line_no - 1], index)
    if line_no < len(numbers) - 1:
        adjacents += find_adjacents_near(numbers[line_no + 1], index)
    return adjacents


def main():
    """Application entry-point."""
    if len(argv) > 1:
        file_name = argv[1]
    else:
        file_name = "puzzle_input.txt"
    schematic = load_schematic(file_name)
    numbers = find_numbers(schematic)
    sum = 0
    for line_no in range(len(schematic)):
        line = schematic[line_no]
        for index in range(1, len(line)):
            if line[index] != "*":
                continue
            adjacents = find_adjacents(numbers, line_no, index)
            if len(adjacents) < 2:
                continue
            sum += int(adjacents[0].group()) * int(adjacents[1].group())
    print(f"sum = {sum}")


if __name__ == "__main__":
    main()
