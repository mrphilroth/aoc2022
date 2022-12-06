#!/usr/bin/env python

from pathlib import Path


def solve(path, n):
    chars = path.open().read()
    for i in range(len(chars)):
        if len(set(chars[i : i + n])) == n:
            print(i + n)
            break


if __name__ == "__main__":
    solve(Path("data/06.txt"), 4)
    solve(Path("data/06.txt"), 14)
