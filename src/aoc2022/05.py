#!/usr/bin/env python

from pathlib import Path
from copy import deepcopy


def setup(lines: list[str]) -> tuple[list[list[str]], list[tuple[int, int, int]]]:
    i_bottom = max([i for i, l in enumerate(lines) if l.find("[") >= 0])
    n_columns = int(1 + len(lines[i_bottom]) / 4)
    grid = [[] for _ in range(n_columns)]
    for i_line in range(i_bottom, -1, -1):
        for i_column in range(n_columns):
            start = 1 + i_column * 4
            if start + 1 < len(lines[i_line]):
                box = lines[i_line][start : start + 1]
                if box != " ":
                    grid[i_column].append(box)

    instructions: list[tuple[int, int, int]] = []
    for i_line in range(i_bottom + 3, len(lines)):
        sline = lines[i_line].strip().split(" ")
        instructions.append((int(sline[1]), int(sline[3]), int(sline[5])))

    return grid, instructions


def first(instructions: list[tuple[int, int, int]], grid: list[list[str]]):
    for ins in instructions:
        for i in range(ins[0]):
            box = grid[ins[1] - 1].pop()
            grid[ins[2] - 1].append(box)

    msg = "".join([stack[-1] for stack in grid])
    print(msg)


def second(instructions: list[tuple[int, int, int]], grid: list[list[str]]):
    for ins in instructions:
        boxes = reversed([grid[ins[1] - 1].pop() for _ in range(ins[0])])
        grid[ins[2] - 1].extend(boxes)

    msg = "".join([stack[-1] for stack in grid])
    print(msg)


if __name__ == "__main__":
    lines = Path("data/05.txt").open().read().splitlines()
    grid, instructions = setup(lines)
    first(instructions, deepcopy(grid))
    second(instructions, deepcopy(grid))
