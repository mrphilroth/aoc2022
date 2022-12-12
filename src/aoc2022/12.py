#!/usr/bin/env python

from pathlib import Path
import numpy as np

lmap = dict(zip("abcdefghijklmnopqrstuvwxyz", range(26)))


def parse(path):
    start = (0, 0)
    end = (0, 0)
    grid = []
    for i, line in enumerate(path.open().readlines()):
        if line.find("S") != -1:
            start = (i, line.find("S"))

        if line.find("E") != -1:
            end = (i, line.find("E"))

        grid.append(
            list(
                map(lambda c: lmap[c], line.strip().replace("S", "a").replace("E", "z"))
            )
        )

    grid = np.array(grid, dtype=np.int32)
    return grid, start, end


def solve(grid, start, end):
    step = 0
    distance = np.ones(grid.shape) * 1e6
    distance[start[0]][start[1]] = 0
    while distance[end[0]][end[1]] == 1e6:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if distance[i][j] == step:
                    if i + 1 < len(grid) and grid[i + 1][j] <= grid[i][j] + 1:
                        distance[i + 1][j] = min(distance[i + 1][j], distance[i][j] + 1)
                    if i - 1 >= 0 and grid[i - 1][j] <= grid[i][j] + 1:
                        distance[i - 1][j] = min(distance[i - 1][j], distance[i][j] + 1)
                    if j + 1 < len(grid[0]) and grid[i][j + 1] <= grid[i][j] + 1:
                        distance[i][j + 1] = min(distance[i][j + 1], distance[i][j] + 1)
                    if j - 1 >= 0 and grid[i][j - 1] <= grid[i][j] + 1:
                        distance[i][j - 1] = min(distance[i][j - 1], distance[i][j] + 1)

        if (distance == step).sum() == 0:
            return 1e6  # No progress. Can't get there from here.

        step += 1

    return step


if __name__ == "__main__":
    grid, start, end = parse(Path("data/12.txt"))
    print(solve(grid, start, end))
    min_steps = 1e6
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                min_steps = min(min_steps, solve(grid, (i, j), end))
    print(min_steps)
