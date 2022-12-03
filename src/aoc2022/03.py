#!/usr/bin/env python

from pathlib import Path

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority = dict(zip(characters, range(1, len(characters) + 1)))


def first(Path):
    sum = 0
    for line in Path.open().read().splitlines():
        ind = int(len(line) / 2)
        overlap = set(line[:ind]).intersection(set(line[ind:])).pop()
        sum += priority[overlap]

    print(sum)


def second(Path):
    sum = 0
    lines = list(Path.open().read().splitlines())
    for i in range(0, len(lines), 3):
        overlap = (
            set(lines[i])
            .intersection(set(lines[i + 1]))
            .intersection(set(lines[i + 2]))
        ).pop()
        sum += priority[overlap]

    print(sum)


if __name__ == "__main__":
    first(Path("data/03.txt"))
    second(Path("data/03.txt"))
