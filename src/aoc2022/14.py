#!/usr/bin/env python

from pathlib import Path
import numpy as np


def print_grid(grid):
    for row in grid.T:
        print("".join(map(str, row)))


def parse(path):
    grid = np.zeros((1000, 179), dtype=int)
    grid[:, 178] = 2
    for line in path.open().read().splitlines():
        pairs = [tuple(map(int, pair.split(","))) for pair in line.split(" -> ")]
        i = 0
        ix, iy = pairs[i]
        while i < len(pairs) - 1:
            while ix != pairs[i + 1][0]:
                grid[ix][iy] = 2
                ix += np.sign(pairs[i + 1][0] - ix)

            while iy != pairs[i + 1][1]:
                grid[ix][iy] = 2
                iy += np.sign(pairs[i + 1][1] - iy)

            grid[ix][iy] = 2
            i += 1

    # print(np.nonzero(grid)[1].max())
    return grid


def fall(grid, x, y) -> tuple[int, int]:
    new_x = x
    ind_nonzero = grid[x, y:].nonzero()[0]
    if len(ind_nonzero) == 0:
        return (-1, -1)

    new_y = y + np.min(ind_nonzero) - 1
    if grid[x - 1, new_y + 1] == 0:
        new_x, new_y = fall(grid, x - 1, new_y + 1)

    elif grid[x + 1, new_y + 1] == 0:
        new_x, new_y = fall(grid, x + 1, new_y + 1)

    return new_x, new_y


def first(grid):
    grid = grid[:, :-1].copy()
    x, y = fall(grid, 500, 0)
    grid[x, y] = 1

    while x != -1 or y != -1:
        x, y = fall(grid, 500, 0)
        if x > 0 and y > 0:
            grid[x, y] = 1

    # print_grid(grid[470:530, :])
    print((grid == 1).sum())


def second(grid):
    x, y = fall(grid, 500, 0)
    grid[x, y] = 1

    while x != 500 or y != 0:
        x, y = fall(grid, 500, 0)
        grid[x, y] = 1

    # print_grid(grid[470:530, :])
    print((grid == 1).sum())


if __name__ == "__main__":
    grid = parse(Path("data/14.txt"))
    # print_grid(grid[470:530, :])
    first(grid)
    second(grid)
