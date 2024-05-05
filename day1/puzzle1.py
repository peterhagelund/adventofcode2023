import re


def main():
    exp = re.compile("[0-9]")
    sum = 0
    with open("puzzle_input.txt", "r") as f:
        for line in f:
            digits = exp.findall(line)
            sum += int(digits[0]) * 10 + int(digits[-1])
    print(f"sum = {sum}")


if __name__ == "__main__":
    main()
