def main():
    num_digits = [str(n) for n in range(1, 10)]
    word_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    digits = num_digits + word_digits
    sum = 0
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            first = sorted(filter(lambda hit: hit[1] != -1, [(digit, line.find(digit)) for digit in digits]), key=lambda hit: hit[1])[0][0]
            last = sorted(filter(lambda hit: hit[1] != -1, [(digit, line.rfind(digit)) for digit in digits]), key=lambda hit: hit[1], reverse=True)[0][0]
            num = 0
            for digit in [first, last]:
                num *= 10
                if digit in num_digits:
                    num += int(digit)
                else:
                    num += word_digits.index(digit) + 1
            sum += num
    print(f"sum = {sum}")


if __name__ == "__main__":
    main()
