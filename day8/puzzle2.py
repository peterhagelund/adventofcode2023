from math import lcm


def find_repeat_cycle(location: str, instructions: str, network: dict[str, tuple[str, str]]) -> list[int]:
    """Finds the repeat cycle of a location.

    Parameters
    ----------
    location : str
        The location.
    instructions : str
        The left/right instructions.
    network : dict[str, tuple[str, str]]
        The network of nodes.

    Returns
    -------
    list[int]
        The results
    """
    ip = -1
    steps = 0
    results: list[int] = []
    while len(results) < 2:
        steps += 1
        ip += 1
        if ip >= len(instructions):
            ip = 0
        instruction = instructions[ip]
        left_right = network[location]
        if instruction == "L":
            location = left_right[0]
        else:
            location = left_right[1]
        if location[2] == "Z":
            results.append(steps)
    return results


def main():
    """Application entry-point."""
    network: dict[str, tuple[str, str]] = {}
    locations: list[str] = []
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            line = line.strip()
            if len(line) == 0:
                continue
            if "=" not in line:
                instructions = line
            else:
                current, left_right = line.split(" = ")
                left, right = left_right[1:-1].split(", ")
                network[current] = (left, right)
                if current[2] == "A":
                    locations.append(current)
    repeats: list[int] = []
    for location in locations:
        results = find_repeat_cycle(location, instructions, network)
        if results[1] % results[0] != 0:
            raise ValueError(f"{location} does not repeat")
        repeats.append(results[0])
    steps = lcm(*repeats)
    print(f"steps = {steps}")


if __name__ == "__main__":
    main()
