#!/usr/bin/env python

from pathlib import Path

from collections import defaultdict

files = dict()
dirs = defaultdict(int)


def solve(path):
    curr_dir = []
    lines = path.open().read().splitlines()
    for line in lines:
        if line.startswith("$ cd"):
            new_dir = line.split(" ")[-1]

            if new_dir == "..":
                curr_dir.pop()

            else:
                curr_dir.append(new_dir)

        elif line.split(" ")[0].isdigit():
            size = int(line.split(" ")[0])
            name = line.split(" ")[1]
            fpath = "/".join(curr_dir + [name])[1:]
            files[fpath] = size

        else:
            pass

    for fpath, size in files.items():
        spath = fpath.split("/")[:-1]
        for i in range(1, len(spath) + 1):
            dirs["/".join(spath[:i])] += size

    sum = 0
    for dir, size in dirs.items():
        if size <= 100000:
            sum += size

    print(sum)

    capacity = 70000000
    target = capacity - 30000000
    min_size = dirs[""] - target
    min_dir = (dirs[""], "")
    for dir, size in dirs.items():
        if size > min_size:
            if size < min_dir[0]:
                min_dir = (size, dir)

    print(min_dir)


if __name__ == "__main__":
    solve(Path("data/07.txt"))
