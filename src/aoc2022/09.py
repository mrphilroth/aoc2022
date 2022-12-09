#!/usr/bin/env python

from pathlib import Path


def first(path):
    positions = set()
    tuples = map(lambda l: l.split(), path.open().read().strip().splitlines())
    tuples = list(map(lambda t: (t[0], int(t[1])), tuples))
    head: list[int] = [0, 0]
    tail: list[int] = [0, 0]

    for dir, steps in tuples:
        for _ in range(steps):
            if dir == "U":
                head[1] += 1
            elif dir == "D":
                head[1] -= 1
            elif dir == "L":
                head[0] -= 1
            elif dir == "R":
                head[0] += 1

            for j in [0, 1]:
                if tail[j] == head[j] - 2:
                    tail[j] += 1
                    tail[(j + 1) % 2] = head[(j + 1) % 2]

                elif tail[j] == head[j] + 2:
                    tail[j] -= 1
                    tail[(j + 1) % 2] = head[(j + 1) % 2]

            positions.add((tail[0], tail[1]))

    print(len(positions))


def second(path):
    positions = set()
    tuples = map(lambda l: l.split(), path.open().read().strip().splitlines())
    tuples = list(map(lambda t: (t[0], int(t[1])), tuples))
    rope: list[list[int]] = [[0, 0] for _ in range(10)]

    for dir, steps in tuples:
        for _ in range(steps):
            if dir == "U":
                rope[0][1] += 1
            elif dir == "D":
                rope[0][1] -= 1
            elif dir == "L":
                rope[0][0] -= 1
            elif dir == "R":
                rope[0][0] += 1

            for knot in range(1, 10):
                if (
                    abs(rope[knot][0] - rope[knot - 1][0]) >= 2
                    or abs(rope[knot][1] - rope[knot - 1][1]) >= 2
                ):
                    rope[knot][0] += max(-1, min(1, rope[knot - 1][0] - rope[knot][0]))
                    rope[knot][1] += max(-1, min(1, rope[knot - 1][1] - rope[knot][1]))

            positions.add((rope[9][0], rope[9][1]))

    print(len(positions))


if __name__ == "__main__":
    first(Path("data/09.txt"))
    second(Path("data/09.txt"))
