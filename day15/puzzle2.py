def hash(value: str) -> int:
    """Calculates the `hash` value of a string.

    For each character in `value` add the ASCII value, multiply by `17` and take remainder of dividing by `256`.

    Parameters
    ----------
    value : str
        The value.

    Returns
    -------
    int
        The `hash`.
    """
    h = 0
    for c in value:
        h += ord(c)
        h *= 17
        h %= 256
    return h


def do_remove(boxes: list[list[tuple[str, int]]], label: str):
    """Handles the removal of a lens.

    Parameters
    ----------
    boxes : list[list[tuple[str, int]]]
        The boxes.
    label : str
        The label of the lens to remove.
    """
    box_index = hash(label)
    box = boxes[box_index]
    lens_index = None
    for i, l in enumerate(box):
        if l[0] == label:
            lens_index = i
            break
    if lens_index is not None:
        del box[lens_index]


def do_add(boxes: list[list[tuple[str, int]]], lens: tuple[str, int]):
    """Handles adding a lens.

    Parameters
    ----------
    boxes : list[list[tuple[str, int]]]
        The boxes.
    lens : tuple[str, int]
        The lens to add.
    """
    box_index = hash(lens[0])
    box = boxes[box_index]
    lens_index = None
    for i, l in enumerate(box):
        if l[0] == lens[0]:
            lens_index = i
            break
    if lens_index is not None:
        box[lens_index] = lens
    else:
        box.append(lens)


def main():
    """Application entry-point."""
    with open("puzzle_input.txt", "rt") as f:
        input = f.read()
    steps = input.split(",")
    boxes: list[list[tuple[str, int]]] = [[] for _ in range(256)]
    for step in steps:
        if "-" in step:
            label, _ = step.split("-")
            do_remove(boxes, label)
        else:
            label, focal_length = step.split("=")
            do_add(boxes, (label, int(focal_length)))
    foxusing_power = 0
    for i, box in enumerate(boxes):
        box_number = i + 1
        for j, lens in enumerate(box):
            slot = j + 1
            power = box_number * slot * lens[1]
            foxusing_power += power
    print(f"focusing power = {foxusing_power}")


if __name__ == "__main__":
    main()
