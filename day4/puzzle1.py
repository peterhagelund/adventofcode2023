from re import compile


def main():
    pattern = compile(r"\d{1,2}")
    sum = 0
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            _, numbers = line[:-1].split(":")
            winning_numbers, my_numbers = numbers.split("|")
            winning_numbers = [int(n) for n in pattern.findall(winning_numbers)]
            my_numbers = [int(n) for n in pattern.findall(my_numbers)]
            points = 0
            for n in my_numbers:
                if n not in winning_numbers:
                    continue
                if points == 0:
                    points = 1
                else:
                    points *= 2
            sum += points
    print(f"sum = {sum}")


if __name__ == "__main__":
    main()
