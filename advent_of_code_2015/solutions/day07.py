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
        ^(?P<X>\w+)?\s*(?P<op>NOT|AND|OR|LSHIFT|RSHIFT)?\s*(?P<Y>\w+)?\s*->\s*(?P<Z>\w+)?$
    """, re.VERBOSE)

    operations = {}
    for line in load_input(day=7).readlines():
        match = re.match(pattern, line)
        if match:
            X = match.group('X')
            op = match.group('op')
            Y = match.group('Y')
            Z = match.group('Z')
            print(op)
            operations[Z] = [
                coalesce(op, 'ASSIGN'),
                coalesce(X, Y),
                Y
            ]
    
    return operations


def resolve(wire, operations={}):

    @cache
    def _resolve(wire):

        if isinstance(wire, int):
            return wire
        
        if wire.isnumeric():
            return int(wire)   

        op, X, Y = operations[wire]

        if op in ['NOT', 'ASSIGN']:
            return LOOKUP[op](_resolve(X))
        else:
            return LOOKUP[op](_resolve(X), _resolve(Y))

    _resolve.cache_clear()

    return _resolve(wire)


def part1():
    '''given the input operations, returns the signal ultimately provided to wire a'''

    # possible fixes to get correct answer:
        # apply uint16 to every input/output
        # print all operations
        # test direct on input rather than test


    a = ctypes.c_uint16(resolve('a', create_input()))
    return a.value
    
def part2():
    ''' '''
    pass


if __name__ == '__main__':
    print(part1())
    print(part2())