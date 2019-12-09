from utils import run
from typing import *


def fuel(mass: int) -> int:
    return mass // 3 - 2


def part1(lines: List[str]) -> str:
    total = 0
    for line in lines:
        total += fuel(int(line))
    return total


def fuel2(mass: int) -> int:
    total = 0
    while True:
        mass2 = fuel(mass)
        if mass2 < 0:
            return total
        total += mass2
        mass = mass2


def part2(lines: List[str]) -> str:
    total = 0
    for line in lines:
        total += fuel2(int(line))
    return total


run(part1, 'day1.txt')
run(part2, 'day1.txt')
