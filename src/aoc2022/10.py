#!/usr/bin/env python

from pathlib import Path


def solve(path):
    X = 1
    cycles = []
    for line in path.open().read().strip().splitlines():
        if line == "noop":
            cycles.append(X)
        if line.startswith("addx"):
            cycles.append(X)
            cycles.append(X)
            X += int(line.split()[1])

    sum = 0
    read = [20, 60, 100, 140, 180, 220]
    for r in read:
        sum += r * cycles[r - 1]

    print(sum)

    drawn = []
    for i in range(240):
        if i % 40 >= cycles[i] - 1 and i % 40 <= cycles[i] + 1:
            drawn.append("#")
        else:
            drawn.append(".")

    for i in range(6):
        print("".join(drawn[i * 40 : (i + 1) * 40]))


if __name__ == "__main__":
    solve(Path("data/10.txt"))
