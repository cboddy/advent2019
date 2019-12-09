import enum
from typing import *

from utils import *


class Opcode(enum.Enum):
    ADD = 1
    MULTIPLY = 2
    HALT = 99


def part1(lines: List[str]) -> str:
    instructions = [int(i)
                    for i in lines[0].split(",")]

    instructions[1] = 12
    instructions[2] = 2

    def _args(idx: int) -> Tuple[int, int]:
        return instructions[instructions[idx+1]], instructions[instructions[idx+2]]

    def _dest(idx: int) -> int:
        return instructions[idx + 3]

    idx = 0
    while True:
        op = Opcode(instructions[idx])
        if op == Opcode.HALT:
            return instructions[0]
        left, right = _args(idx)
        dest = _dest(idx)
        if op == Opcode.ADD:
            instructions[dest] = left + right
        elif op == Opcode.MULTIPLY:
            instructions[dest] = left * right
        else:
            raise ValueError()
        idx += 4


run(part1, 'day2.txt')
