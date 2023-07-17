import ctypes
import operator
import re
from collections import namedtuple
from dataclasses import dataclass

from helper import coalesce, load_input

# Needs restructure as not working as implied:
    # Need to convert instructions to dictoinary
    # and then recurse through values etc in order to get desired values

class Operation:

    def __init__(self):
        self._attrs = {}
        self._lookup: dict={
            'AND': operator.and_,
            'OR': operator.or_,
            'LSHIFT': operator.lshift,
            'RSHIFT': operator.rshift,
            'NOT': operator.invert,
            'ASSIGN': lambda X: X,
        }
        
    def __getattr__(self, name):
        if name.startswith("_"):
            super().__getattr__(name)
        if name in self._attrs:
            return self._attrs[name].value
        else:
            return int(name)

    def __setattr__(self, name, value):
        if name.startswith("_"):
            super().__setattr__(name, value)
        else:
            self._attrs[name] = ctypes.c_uint16(value)

    # def _resolve(self, a):
    #     '''
    #     Given argument a, which could be an attribute or number, 
    #     returns either the associated attribute or 
    #     returns integer representation of number
    #     '''
    #     try:
    #         return int(a)
    #     except ValueError:
    #         return getattr(self, a)
    #     except TypeError:
    #         return getattr(self, a)
    
    def apply(self, operation: namedtuple):
        if operation.operator in ['ASSIGN', 'NOT']:
            setattr(
                self, 
                operation.Z, 
                self._lookup[operation.operator](
                    getattr(self, operation.X)
                )
            )
        else:
            setattr(
                self, 
                operation.Z, 
                self._lookup[operation.operator](
                    getattr(self, operation.X),
                    getattr(self, operation.Y),
                )
            )
        


def create_input():
    '''
    read in puzzle input from file, 
    using regex to extract coordinates & instruction for each line
    and returning a list of intructions/coordinates stored as named tuples
    '''
    Operation = namedtuple("Operation", ["operator", "X", "Y", "Z"])
    operations = []

    pattern = re.compile(r"""

        # first arguments either number, variable or NOT operator
        ^(\d+)?\s*(NOT)?\s*(\w+)?  

        # AND/OR/LSHIFT/RSHIFT followed by number or string
        \s*(AND|OR|LSHIFT|RSHIFT)?\s*(\w+)?
        
        # assignment to variable
        \s*->?\s*(\w+)?$

    """, re.VERBOSE)

    for line in load_input(day=7).readlines():
        match = re.match(pattern, line)
        if match:
            X1, op1, X2, op2, Y1, Z = match.groups()
            operations.append(Operation(
                operator = coalesce(op1, op2, 'ASSIGN'),
                X = coalesce(X1, X2),
                Y = Y1,
                Z = Z
            ))
    
    return operations

def part1():
    '''given the input operations, returns the signal ultimately provided to wire a'''
    op = Operation()
    for operation in create_input():
        op.apply(operation)
    return op.a
    
def part2():
    ''' '''
    pass


if __name__ == '__main__':
    print(part1())
    print(part2())