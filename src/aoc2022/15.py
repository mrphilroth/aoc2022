#!/usr/bin/env python

from pathlib import Path


def parse(path):
    sensors = []
    beacons = []
    for line in path.open().read().splitlines():
        sline = line.split(" ")
        sensors.append(tuple(map(lambda s: int(s[2:].strip(":,")), sline[2:4])))
        beacons.append(tuple(map(lambda s: int(s[2:].strip(":,")), sline[8:10])))

    return sensors, beacons


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
    return merged


def in_intervals(x: int, intervals: list[tuple[int, int]]) -> bool:
    for interval in intervals:
        if interval[0] <= x <= interval[1]:
            return True
    return False


def size_of_intervals(intervals: list[tuple[int, int]]) -> int:
    return sum([interval[1] - interval[0] + 1 for interval in intervals])


def invert_intervals(
    intervals: list[tuple[int, int]], lower_limit: int = 0, upper_limit: int = 4000000
) -> list[tuple[int, int]]:
    intervals.sort(key=lambda x: x[0])
    inverted = []
    if intervals[0][0] > lower_limit:
        inverted.append((lower_limit, intervals[0][0] - 1))
    for i in range(len(intervals) - 1):
        inverted.append((intervals[i][1] + 1, intervals[i + 1][0] - 1))
    if intervals[-1][1] < upper_limit:
        inverted.append((intervals[-1][1] + 1, upper_limit))
    return inverted


def check_for_gaps(sensors, beacons, row):
    intervals = []
    for i in range(len(sensors)):
        distance = abs(sensors[i][0] - beacons[i][0]) + abs(
            sensors[i][1] - beacons[i][1]
        )
        to_row = abs(sensors[i][1] - row)
        if to_row <= distance:
            leftover = distance - to_row
            intervals.append((sensors[i][0] - leftover, sensors[i][0] + leftover))

    intervals = merge_intervals(intervals)
    return invert_intervals(intervals)


def first(sensors, beacons):
    intervals = []
    beacons_in_row = set()
    for i in range(len(sensors)):
        distance = abs(sensors[i][0] - beacons[i][0]) + abs(
            sensors[i][1] - beacons[i][1]
        )
        to_row = abs(sensors[i][1] - 2000000)
        if to_row <= distance:
            leftover = distance - to_row
            intervals.append((sensors[i][0] - leftover, sensors[i][0] + leftover))

        if beacons[i][1] == 2000000:
            beacons_in_row.add(beacons[i][0])

    size = size_of_intervals(merge_intervals(intervals))
    for beacon_in_row in beacons_in_row:
        if in_intervals(beacon_in_row, intervals):
            size -= 1

    print(size)


def second(sensors, beacons):
    for row in range(0, 4000000):
        result = check_for_gaps(sensors, beacons, row)
        if result:
            print(result[0][0] * 4000000 + row)
            break


if __name__ == "__main__":
    sensors, beacons = parse(Path("data/15.txt"))
    first(sensors, beacons)  # 5335787
    second(sensors, beacons)  # 13673971349056
