import re


def main():
    digits = [str(n) for n in range(1, 10)]
    exp = re.compile("|".join(digits))
    sum = 0
    with open("puzzle_input.txt", "r") as f:
        for line in f:
            digits = exp.findall(line)
            first = digits[0]
            last = digits[-1]
            sum += int(first) * 10 + int(last)
    print(f"sum = {sum}")


if __name__ == "__main__":
    main()
