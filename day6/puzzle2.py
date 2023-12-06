def main():
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            if line.startswith("Time:"):
                time = int(line[5:].strip().replace(" ", ""))
            elif line.startswith("Distance:"):
                distance = int(line[9:].strip().replace(" ", ""))
            else:
                continue
    options = 0
    for hold_time in range(time):
        speed = hold_time
        d = (time - hold_time) * speed
        if d > distance:
            options += 1
    print(f"options = {options}")


if __name__ == "__main__":
    main()
