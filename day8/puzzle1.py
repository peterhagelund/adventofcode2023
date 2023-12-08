def main():
    """Application entry-point."""
    network: dict[str, tuple[str, str]] = {}
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
    location = "AAA"
    ip = -1
    steps = 0
    while location != "ZZZ":
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
    print(f"steps = {steps}")


if __name__ == "__main__":
    main()
