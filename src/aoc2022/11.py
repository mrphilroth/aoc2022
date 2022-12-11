#!/usr/bin/env python

from collections.abc import Callable
from dataclasses import dataclass


@dataclass
class Monkey:
    items: list[int]
    operation: Callable[[int], int]
    test: Callable[[int], int]
    inspections: int = 0


def get_monkeys():
    return [
        Monkey(
            [56, 56, 92, 65, 71, 61, 79],
            lambda x: x * 7,
            lambda x: 3 if x % 3 == 0 else 7,
        ),
        Monkey([61, 85], lambda x: x + 5, lambda x: 6 if x % 11 == 0 else 4),
        Monkey([54, 96, 82, 78, 69], lambda x: x * x, lambda x: 0 if x % 7 == 0 else 7),
        Monkey([57, 59, 65, 95], lambda x: x + 4, lambda x: 5 if x % 2 == 0 else 1),
        Monkey([62, 67, 80], lambda x: x * 17, lambda x: 2 if x % 19 == 0 else 6),
        Monkey([91], lambda x: x + 7, lambda x: 1 if x % 5 == 0 else 4),
        Monkey(
            [79, 83, 64, 52, 77, 56, 63, 92],
            lambda x: x + 6,
            lambda x: 2 if x % 17 == 0 else 0,
        ),
        Monkey(
            [50, 97, 76, 96, 80, 56], lambda x: x + 3, lambda x: 3 if x % 13 == 0 else 5
        ),
    ]


divisors = [2, 3, 5, 7, 11, 13, 17, 19]
modulo = 1
for divisor in divisors:
    modulo *= divisor


def solve(monkeys, nrounds, part=1):
    for _ in range(nrounds):
        for i, monkey in enumerate(monkeys):
            for _ in range(len(monkey.items)):
                monkey.inspections += 1
                item = monkey.items.pop(0)
                item = monkey.operation(item)
                if part == 1:
                    item = int(item / 3)
                else:
                    item = item % modulo

                new_monkey = monkey.test(item)
                monkeys[new_monkey].items.append(item)

    inspections = sorted(list(monkey.inspections for monkey in monkeys))
    print(inspections[-1] * inspections[-2])


if __name__ == "__main__":
    solve(get_monkeys(), 20, 1)
    solve(get_monkeys(), 10000, 2)
