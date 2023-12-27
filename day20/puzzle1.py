from collections import deque


def main():
    with open("puzzle_input.txt", "rt") as f:
        modules = {}
        for line in f:
            source, destinations = line.strip().split(" -> ")
            destinations = [d.strip() for d in destinations.split(",")]
            name = None
            type = None
            if source[0] in "%&":
                type = source[0]
                name = source[1:]
            else:
                name = source
            if name in modules:
                module = modules[name]
            else:
                module = {
                    "name": name,
                }
                modules[name] = module
            module["type"] = type
            module["destinations"] = destinations
            for d in destinations:
                if d not in modules:
                    modules[d] = {
                        "name": d,
                        "type": None,
                        "destinations": [],
                    }
    for name, module in modules.items():
        if module["type"] == "%":
            module["state"] = "off"
        for d in module["destinations"]:
            if modules[d]["type"] == "&":
                modules[d][name] = "low"
    queue = deque()
    low_count = 0
    high_count = 0
    for _ in range(1000):
        queue.append(("button", "low", "broadcaster"))
        while queue:
            source, pulse, destination = queue.popleft()
            if pulse == "low":
                low_count += 1
            else:
                high_count += 1
            module = modules[destination]
            if module["type"] == "%":
                if pulse == "low":
                    _state, _pulse = ("on", "high") if module["state"] == "off" else ("off", "low")
                    module["state"] = _state
                    for _destination in module["destinations"]:
                        queue.append((destination, _pulse, _destination))
            elif module["type"] == "&":
                module[source] = pulse
                low = 0
                high = 0
                for k, v in module.items():
                    if k[0] == "_":
                        continue
                    if v == "low":
                        low += 1
                    else:
                        high += 1
                if high > 0 and low == 0:
                    _pulse = "low"
                else:
                    _pulse = "high"
                for _destination in module["destinations"]:
                    queue.append((destination, _pulse, _destination))
            else:
                for _destination in module["destinations"]:
                    queue.append((destination, pulse, _destination))
    print(f"product = {low_count * high_count}")


if __name__ == "__main__":
    main()
