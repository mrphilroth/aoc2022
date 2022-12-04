#!/usr/bin/env python

from pathlib import Path


def first(Path):
    sum = 0
    for line in Path.open().read().splitlines():
        pair = map(lambda s: list(map(int, s.split("-"))), line.split(","))
        sets = list(map(lambda p: set(range(p[0], p[1] + 1)), pair))
        sets = sorted(sets, key=lambda s: len(s))
        if len(sets[0].intersection(sets[1])) == len(sets[0]):
            sum += 1

    print(sum)


def second(Path):
    sum = 0
    for line in Path.open().read().splitlines():
        pair = map(lambda s: list(map(int, s.split("-"))), line.split(","))
        sets = list(map(lambda p: set(range(p[0], p[1] + 1)), pair))
        if len(sets[0].intersection(sets[1])) > 0:
            sum += 1

    print(sum)

    pass


if __name__ == "__main__":
    first(Path("data/04.txt"))
    second(Path("data/04.txt"))
