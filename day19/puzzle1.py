def main():
    workflows: dict[str, list[tuple[str, str, int, str]]] = {}
    parts: list[dict[str, int]] = []
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            line = line.strip()
            index = line.find("{")
            if index == -1:
                continue
            if index == 0:
                categories = line[1:-1].split(",")
                part: dict[str, int] = {}
                for category in categories:
                    name, value = category.split("=")
                    part[name] = int(value)
                parts.append(part)
            else:
                name = line[:index]
                rules: list[tuple[str, str, int, str]] = []
                for rule in line[index + 1 : -1].split(","):
                    category = None
                    operator = None
                    value = None
                    destination = None
                    if ":" in rule:
                        predicate, destination = rule.split(":")
                        category = predicate[0]
                        assert category in "xmas"
                        operator = predicate[1]
                        assert operator in "<>"
                        value = int(predicate[2:])
                    else:
                        destination = rule
                    rules.append((category, operator, value, destination))
                workflows[name] = rules
    accepted: list[dict[str, int]] = []
    rejected: list[dict[str, int]] = []
    for part in parts:
        name = "in"
        while True:
            rules = workflows[name]
            destination = None
            for rule in rules:
                if rule[1] is None:
                    destination = rule[3]
                    break
                else:
                    category = rule[0]
                    operator = rule[1]
                    value = rule[2]
                    if operator == "<" and part[category] < value:
                        destination = rule[3]
                    elif operator == ">" and part[category] > value:
                        destination = rule[3]
                if destination is not None:
                    break
            if destination == "A":
                accepted.append(part)
                break
            elif destination == "R":
                rejected.append(part)
                break
            else:
                name = destination
    total = 0
    for part in accepted:
        total += sum(part.values())
    print(f"total = {total}")


if __name__ == "__main__":
    main()
