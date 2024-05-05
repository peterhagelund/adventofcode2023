def main():
    num_digits = [str(n) for n in range(1, 10)]
    word_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] 
    digits = num_digits + word_digits
    sum = 0
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            first_index = len(line)
            first = None
            last_index = -1
            last = None
            for digit in digits:
                index = line.find(digit)
                if index == -1:
                    continue
                if index < first_index:
                    first_index = index
                    first = digit
                index = line.rfind(digit)
                if index == -1:
                    continue
                if index > last_index:
                    last_index = index
                    last = digit
            num = 0
            if first in num_digits:
                num = int(first)
            else:
                num = word_digits.index(first) + 1
            num *= 10
            if last in num_digits:
                num += int(last)
            else:
                num += word_digits.index(last) + 1
            sum += num
    print(f"sum = {sum}")


if __name__ == "__main__":
    main()
