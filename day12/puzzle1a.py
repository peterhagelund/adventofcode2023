def find_arrangements(conditions: str, sizes: list[int], c_index: int, s_index: int, size: int) -> int:
    if c_index == len(conditions):
        if s_index == len(sizes) and size == 0:
            return 1
        elif s_index == len(sizes) - 1 and sizes[s_index] == size:
            return 1
        else:
            return 0
    result = 0
    for c in [".", "#"]:
        if conditions[c_index] not in [c, "?"]:
            continue
        if c == "." and size == 0:
            result += find_arrangements(conditions, sizes, c_index + 1, s_index, 0)
        elif c == "." and size > 0 and s_index < len(sizes) and sizes[s_index] == size:
            result += find_arrangements(conditions, sizes, c_index + 1, s_index + 1, 0)
        elif c == "#":
            result += find_arrangements(conditions, sizes, c_index + 1, s_index, size + 1)
    return result


def main():
    """Application entry-point."""
    records: list[tuple[str, list[int]]] = []
    with open("sample_input.txt", "rt") as f:
        for line in f:
            conditions, sizes = line.strip().split(" ")
            sizes = [int(size) for size in sizes.split(",")]
            records.append((conditions, sizes))
    sum = 0
    for row in records:
        sum += find_arrangements(row[0], row[1], 0, 0, 0)
    print(f"sum = {sum}")


if __name__ == "__main__":
    main()
