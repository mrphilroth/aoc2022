#!/usr/bin/env python

from pathlib import Path

translate = {"X": "A", "Y": "B", "Z": "C"}
shape_points = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}


def outcome(opp: str, me: str) -> int:
    me_tmp = translate[me]
    if opp == me_tmp:
        return 3

    if opp == "A":
        if me_tmp == "B":
            return 6

    elif opp == "B":
        if me_tmp == "C":
            return 6

    if opp == "C":
        if me_tmp == "A":
            return 6

    return 0


def first(Path):
    score = 0
    for line in Path.open().read().splitlines():
        opp, me = line.split()
        score += outcome(opp, me) + shape_points[me]

    print(score)


outcome_points = {"X": 0, "Y": 3, "Z": 6}
int_to_shape = {0: "A", 1: "B", 2: "C"}
shape_to_int = {"A": 0, "B": 1, "C": 2}


def shape(opp: str, me: str) -> int:
    if me == "Y":
        return shape_points[opp]

    opp_int = shape_to_int[opp]
    if me == "X":
        return shape_points[int_to_shape[(opp_int - 1) % 3]]

    return shape_points[int_to_shape[(opp_int + 1) % 3]]


def second(Path):
    score = 0
    for line in Path.open().read().splitlines():
        opp, me = line.split()
        score += outcome_points[me] + shape(opp, me)

    print(score)


if __name__ == "__main__":
    first(Path("data/02.txt"))
    second(Path("data/02.txt"))
