from re import compile


def main():
    pattern = compile(r"\d+")
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            if line.startswith("Time:"):
                times = [int(t) for t in pattern.findall(line)]
            elif line.startswith("Distance:"):
                distances = [int(t) for t in pattern.findall(line)]
            else:
                continue
    travels: list[int] = []
    for i in range(len(times)):
        options = 0
        for hold_time in range(times[i]):
            speed = hold_time
            distance = (times[i] - hold_time) * speed
            if distance > distances[i]:
                options += 1
        travels.append(options)
    margin_of_error = 1
    for travel in travels:
        margin_of_error *= travel
    print(f"margin of error = {margin_of_error}")


if __name__ == "__main__":
    main()
