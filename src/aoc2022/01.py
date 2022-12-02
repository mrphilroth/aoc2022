#!/usr/bin/env python

from pathlib import Path

import numpy as np


def calories(path):
    input = path.open().read()
    elves = [np.array(list(map(int, elf.split("\n")))) for elf in input.split("\n\n")]
    sums = np.array([elf.sum() for elf in elves])
    i_sums = np.argsort(sums)
    print(i_sums[-1], sums[i_sums[-1]])
    print(i_sums[-3:], sums[i_sums[-3:]].sum())


if __name__ == "__main__":
    calories(Path("data/calories.txt"))
