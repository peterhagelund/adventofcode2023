import re


def main():
    schematic = []
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            schematic.append(line[:-1])
    pattern = re.compile(r"[0-9]{1,3}")
    line_count = len(schematic)
    sum = 0
    line_no = 0
    for line in schematic:
        length = len(line)
        for match in pattern.finditer(line):
            is_part = False
            start = match.start()
            end = match.end()
            if start > 0 and line[start - 1] != ".":
                is_part = True
            if end < length and line[end] != ".":
                is_part = True
            if not is_part:
                if start > 0:
                    start -= 1
                if end == length:
                    end -= 1
                if line_no > 0:
                    for index in range(start, end + 1):
                        if schematic[line_no - 1][index] != "." and not schematic[line_no - 1][index].isdigit():
                            is_part = True
                            break
                if line_no < line_count - 1:
                    for index in range(start, end + 1):
                        if schematic[line_no + 1][index] != "." and not schematic[line_no + 1][index].isdigit():
                            is_part = True
                            break
            if is_part:
                sum += int(match.group())
        line_no += 1
    print(f"sum = {sum}")


if __name__ == "__main__":
    main()
