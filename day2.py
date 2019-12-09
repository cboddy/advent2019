import enum
from typing import *

import utils


class Opcode(enum.Enum):
    ADD = 1
    MULTIPLY = 2
    HALT = 99


def _instructions(line: str) -> List[int]:
    return [int(i)
            for i in line.split(",")]


def day2(instructions: List[int], noun: int = 12, verb: int = 2) -> str:
    instructions[1] = noun
    instructions[2] = verb

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


def day2_part2():
    instructions = _instructions(utils._read_one('day2.txt'))
    for noun in range(100):
        for verb in range(100):
            value = day2(list(instructions), noun, verb)
            if value == 19690720:
                print(noun * 100 + verb)


# part 1
day2(_instructions(utils._read_one('day2.txt')))

# part 2
day2_part2()
