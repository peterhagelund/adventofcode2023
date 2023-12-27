from collections import deque


def main():
    with open("puzzle_input.txt", "rt") as f:
        modules = {}
        for line in f:
            source, destinations = line.strip().split(" -> ")
            destinations = [d.strip() for d in destinations.split(",")]
            _name = None
            _type = None
            if source[0] in "%&":
                _type = source[0]
                _name = source[1:]
            else:
                _name = source
            if _name in modules:
                module = modules[_name]
            else:
                module = {
                    "_name": _name,
                }
                modules[_name] = module
            module["_type"] = _type
            module["_destinations"] = destinations
            for d in destinations:
                if d not in modules:
                    modules[d] = {
                        "_name": d,
                        "_type": None,
                        "_destinations": [],
                    }
    for name, module in modules.items():
        if module["_type"] == "%":
            module["_state"] = "off"
        for d in module["_destinations"]:
            if modules[d]["_type"] == "&":
                modules[d][name] = "low"
    queue = deque()
    presses = 0
    while True:
        queue.append(("button", "low", "broadcaster"))
        presses += 1
        while queue:
            source, pulse, destination = queue.popleft()
            pulse_count += 1
            module = modules[destination]
            if module["_type"] == "%":
                if pulse == "low":
                    _state, _pulse = ("on", "high") if module["_state"] == "off" else ("off", "low")
                    module["_state"] = _state
                    for _destination in module["_destinations"]:
                        queue.append((destination, _pulse, _destination))
            elif module["_type"] == "&":
                module[source] = pulse
                _low = 0
                _high = 0
                for k, v in module.items():
                    if k[0] == "_":
                        continue
                    if v == "low":
                        _low += 1
                    else:
                        _high += 1
                if _high > 0 and _low == 0:
                    _pulse = "low"
                else:
                    _pulse = "high"
                for _destination in module["_destinations"]:
                    queue.append((destination, _pulse, _destination))
            else:
                module["_pulse"] = pulse
                for _destination in module["_destinations"]:
                    queue.append((destination, pulse, _destination))
        if presses % 1000000 == 0:
            print(presses)
        rx = modules["rx"]
        if "_pulse" in rx and rx["_pulse"] == "low":
            print(rx, pulse_count)
            break
    print(f"presses = {presses}")


if __name__ == "__main__":
    main()
