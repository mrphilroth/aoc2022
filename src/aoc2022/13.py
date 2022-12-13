#!/usr/bin/env python

from pathlib import Path

from functools import cmp_to_key


def compare(left, right) -> int:
    i = 0
    while i < len(left) and i < len(right):
        loop = 0
        if type(left[i]) == int and type(right[i]) == int:
            loop = left[i] - right[i]
        elif type(left[i]) == list and type(right[i]) == list:
            loop = compare(left[i], right[i])
        else:
            if type(left[i]) == int:
                loop = compare([left[i]], right[i])
            else:
                loop = compare(left[i], [right[i]])

        if loop != 0:
            return loop

        i += 1

    if i == len(left) and i == len(right):
        return 0

    elif i == len(left):
        return -1

    else:
        #  i == len(right):
        return 1


def first(path):
    pairs = path.open().read().split("\n\n")

    sum = 0
    for i, pair in enumerate(pairs):
        left, right = map(eval, pair.split("\n"))
        if compare(left, right) < 0:
            sum += i + 1

    print(sum)


def second(path):
    packets = list(
        map(eval, filter(lambda l: len(l) > 0, path.open().read().split("\n")))
    )
    packets.extend([[[2]], [[6]]])
    packets.sort(key=cmp_to_key(compare))
    print((1 + packets.index([[2]])) * (1 + packets.index([[6]])))


if __name__ == "__main__":
    first(Path("data/13.txt"))
    second(Path("data/13.txt"))
