import collections
import itertools
import enum
from typing import *
from day5 import run
import itertools
import utils

def run_amp(phase_settings: List[int], memory: List[int]) -> List[int]:
    last_output = 0
    all_outputs = []
    for phase in phase_settings:
        inputs = [phase, last_output]
        #outputs = run(list(memory), inputs)
        outputs = run(memory, inputs)
        #import pdb; pdb.set_trace() # BREAKPOINT
        last_output  = outputs[-1]
        all_outputs.append(outputs[-1])
    return all_outputs

def test():
    #memory=[3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
    #phase_settings = range(5)
    memory=[3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    phase_settings=list(range(5))[::-1]
    out = run_amp(phase_settings, memory)
    print("phase_settings", phase_settings, "outputs", out)
    last_out  = out[-1]
    max_out  = -1e99
    if last_out > max_out:
        max_out = last_out
    print(max_out)


test()
    

