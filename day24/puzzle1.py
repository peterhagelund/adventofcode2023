position = tuple[int, int, int]
velocity = tuple[int, int, int]
coefficients = tuple[int, int, int]
hailstone = tuple[position, velocity, coefficients]

POS = 0
VEL = 1
COF = 2

X = 0
Y = 1
Z = 2

A = 0
B = 1
C = 2


def main():
    """Application entry-point."""
    hailstones: list[hailstone] = []
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            pos, vel = line.strip().split("@")
            pos = tuple([int(p.strip()) for p in pos.split(",")])
            vel = tuple([int(v.strip()) for v in vel.split(",")])
            # The formula for calculating the intersection between two lines
            # represented as a1x + b1y + c1 = 0 and a2x + b2y + c2 is:
            #
            # x = (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1)
            # y = (c1 * a2 - c2 * a1) / (a1 * b2 - a2 * b1)
            #
            # See: https://unacademy.com/content/point-of-intersection-formula/#:~:text=The%20point%20of%20intersection%20formula,of%20three%20or%20more%20lines.
            #
            # The input file has x = t * vx + px and y = t * vy + py, so:
            # a = vx
            # b = -vy
            # c = vy * px - vx * py
            cof = (vel[Y], -vel[X], vel[Y] * pos[X] - vel[X] * pos[Y])
            hailstones.append((pos, vel, cof))
    intersections = 0
    for i, hs1 in enumerate(hailstones):
        for hs2 in hailstones[:i]:
            a1, b1, c1 = hs1[COF][A], hs1[COF][B], hs1[COF][C]
            a2, b2, c2 = hs2[COF][A], hs2[COF][B], hs2[COF][C]
            if a1 * b2 == b1 * a2:
                continue  # Parallel; skip
            x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
            y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
            if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000:
                if all((x - hs[POS][X]) * hs[VEL][X] >= 0 and (y - hs[POS][Y]) * hs[VEL][Y] >= 0 for hs in (hs1, hs2)):
                    intersections += 1
    print(f"intersections = {intersections}")


if __name__ == "__main__":
    main()
