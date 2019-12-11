import collections
import enum
from typing import *

import utils

_INSTRUCTION_PARAMS = ['op_code', 'ip', 'param_modes']


class Opcode(enum.Enum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE=5
    JUMP_IF_FALSE=6
    LESS_THAN=7
    EQUALS=8
    HALT = 99
    
    def n_params(self):
        if self in (Opcode.ADD, Opcode.MULTIPLY, Opcode.LESS_THAN, Opcode.EQUALS):
            return 3
        if self in (Opcode.JUMP_IF_TRUE, Opcode.JUMP_IF_FALSE):
            return 2
        if self in (Opcode.INPUT, Opcode.OUTPUT):
            return 1
        if self == Opcode.HALT:
            return 0


class Mode(enum.Enum):
    POSITION = 0
    IMMEDIATE = 1


class Instruction(collections.namedtuple('Instruction', _INSTRUCTION_PARAMS)):

    def is_finished(self):
        return self.op_code == Opcode.HALT

    def get_arg(self, pos: int, memory:  List[int]) -> int:
        mode = self.param_modes[pos]
        param = memory[self.ip+1+pos]
        if mode == Mode.IMMEDIATE:
            return param
        if mode == Mode.POSITION:
            return memory[param]

    def get_dest(self, pos: int, memory: List[int]) -> int:
        return memory[self.ip+1+pos]

    def process(self, memory: List[int], inputs: List[int], outputs: List[int]) -> Optional[int]:
        """Optionally returns anip to jump to"""
        print(f'Instruction {self}')
        op = self.op_code
        if op == Opcode.HALT:
            pass
        elif op in (Opcode.ADD, Opcode.MULTIPLY, Opcode.LESS_THAN, Opcode.EQUALS):
            left = self.get_arg(0, memory)
            right = self.get_arg(1, memory)
            dest = self.get_dest(2, memory)
            if op == Opcode.ADD:
                value = left + right
            elif op == Opcode.MULTIPLY:
                value = left * right
            elif op == Opcode.LESS_THAN:
                value = 1 if left < right else 0
                memory[dest] = value
            elif op == Opcode.EQUALS:
                value = 1 if left == right else 0
            else:
                raise ValueError()
            memory[dest] = value

        elif op == Opcode.INPUT:
            dest = self.get_dest(0, memory)
            memory[dest] = inputs.pop()
        elif op == Opcode.OUTPUT:
            arg = self.get_dest(0, memory)
            output = memory[arg]
            outputs.append(output)
            print(f'Output {output}')
        elif op in (Opcode.JUMP_IF_TRUE, Opcode.JUMP_IF_FALSE):
            param = self.get_arg(0, memory)
            dest = self.get_dest(1, memory)
            if op == Opcode.JUMP_IF_TRUE:
                do_jump = param > 0
            elif op == Opcode.JUMP_IF_FALSE:
                do_jump = param == 0
            else: 
                raise ValueError()
            if do_jump:
                return dest
        else:
            raise ValueError()

    def parse(values: List[int], ip: int):
        value = values[ip]
        op_code = Opcode(value % 100)
        mode_param_1 = Mode(value//100 % 10)
        mode_param_2 = Mode(value//1000 % 10)
        mode_param_3 = Mode(value//10000 % 10)
        param_modes = [mode_param_1, mode_param_2, mode_param_3]
        n_params = op_code.n_params()
        return Instruction(op_code, ip, param_modes)


def _instructions(line: str) -> List[int]:
    return [int(i)
            for i in line.split(",")]


def day5(memory: List[int], inputs: List[int]) -> str:
    ip = 0
    outputs = []
    while True:
        instr = Instruction.parse(memory, ip)
        jump_ip = instr.process(memory, inputs, outputs)
        if instr.is_finished():
            break
        if jump_ip is None:
            ip += 1+instr.op_code.n_params()
        else:
            ip = jump_ip


#day5(_instructions(utils._read_one('day5.txt')), [1])
day5(_instructions(utils._read_one('day5_pt2.txt')), [5])
