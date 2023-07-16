import re
from collections import namedtuple
from dataclasses import dataclass, field
from types import MappingProxyType

import numpy as np
from helper import load_input


class Lights:

    fn_lookup: dict={
        # complete me
    }

    def __init__(self):
        self.arr: np.ndarray = np.zeros((1000, 1000), dtype=bool)
    
    def apply(self, instruction):
        # complete me
        pass



def create_input():
    '''
    read in puzzle input from file, 
    using regex to extract coordinates & instruction for each line
    and returning a list of intructions/coordinates stored as named tuples
    '''
    Instruction = namedtuple("Instruction", ["instruction", "x1", "y1", "x2", "y2"])
    instructions = []

    for line in load_input(day=6).readlines():
        match = re.match(r"^(toggle|turn on|turn off) (\d+),(\d+) through (\d+),(\d+)$", line)
        if match:
            instructions.append(Instruction(
                instruction=match.group(1), 
                x1=int(match.group(2)), 
                y1=int(match.group(3)), 
                x2=int(match.group(4)), 
                y2=int(match.group(5))
            ))
    
    return instructions



def part1():
    '''return the number of lit lights after following instructions'''
    # loop through instructions and apply to lights
    pass

def part2():
    '''  '''
    pass


if __name__ == '__main__':
    print(part1())
    print(part2())