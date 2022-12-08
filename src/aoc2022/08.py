#!/usr/bin/env python

from pathlib import Path

import numpy as np


def read(path):
    lines = path.open().read().splitlines()
    pgrid = list(map(lambda l: list(map(int, l)), lines))
    grid = np.array(pgrid, dtype=np.int32)
    return grid


def first(grid):
    visible = 0
    h, w = grid.shape
    for i in range(h):
        for j in range(w):
            height = grid[i, j]
            if i == 0 or i == h - 1 or j == 0 or j == w - 1:
                visible += 1
            else:
                if (
                    grid[i, j + 1 :].max() < height
                    or grid[i, :j].max() < height
                    or grid[i + 1 :, j].max() < height
                    or grid[:i, j].max() < height
                ):
                    visible += 1
    print(visible)


def visible(a, h):
    logical = a < h
    if logical.sum() == len(a):
        return len(a)

    return logical[: np.argmin(logical)].sum() + 1


def second(path):
    max_scenic = 0
    h, w = grid.shape
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            height = grid[i, j]
            v1 = visible(grid[i, j + 1 :], height)
            v2 = visible(grid[i, j - 1 :: -1], height)
            v3 = visible(grid[i + 1 :, j], height)
            v4 = visible(grid[i - 1 :: -1, j], height)
            scenic = v1 * v2 * v3 * v4

            if scenic > max_scenic:
                max_scenic = scenic

    print(max_scenic)


if __name__ == "__main__":
    grid = read(Path("data/08.txt"))
    first(grid)
    second(grid)
