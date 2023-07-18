import ctypes
import operator
import re
from collections import namedtuple
from dataclasses import dataclass
from functools import cache

from helper import coalesce, load_input


LOOKUP = {
    'AND': operator.and_,
    'OR': operator.or_,
    'LSHIFT': operator.lshift,
    'RSHIFT': operator.rshift,
    'NOT': operator.invert,
    'ASSIGN': lambda Z: Z,
}      


def create_input():
    '''
    read in puzzle input from file, 
    using regex to extract coordinates & instruction for each line
    and returning a dictionary with list of input intructions/coordinates
    '''
    pattern = re.compile(r"""

        # first arguments either number, variable or NOT operator
        ^(\d+)?\s*(NOT)?\s*(\w+)?  

        # AND/OR/LSHIFT/RSHIFT followed by number or string
        \s*(AND|OR|LSHIFT|RSHIFT)?\s*(\w+)?
        
        # assignment to variable
        \s*->?\s*(\w+)?$

    """, re.VERBOSE)

    operations = {}
    for line in load_input(day=7).readlines():
        match = re.match(pattern, line)
        if match:
            X1, op1, X2, op2, Y1, Z = match.groups()
            operations[Z] = [
                coalesce(op1, op2, 'ASSIGN'),
                coalesce(X1, X2),
                Y1
            ]
    
    return operations


@cache
def resolve(wire):

    if isinstance(wire, int):
        return wire
    
    if wire.isnumeric():
        return int(wire)   

    op, X, Y = operations[wire]
    print(op)
    if op in ['NOT', 'ASSIGN']:
        return LOOKUP[op](resolve(X))
    else:
        return LOOKUP[op](resolve(X), resolve(Y))

    

    


def part1():
    '''given the input operations, returns the signal ultimately provided to wire a'''
    op = Operation()
    for operation in create_input():
        op.apply(operation)
    return op.a

    # ctypes.c_uint16(Z)
    
def part2():
    ''' '''
    pass


if __name__ == '__main__':
    print(part1())
    print(part2())