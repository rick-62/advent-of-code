import ctypes
import operator
import re
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
        ^(?P<X>\w+)*?\s*(?P<op>NOT|AND|OR|LSHIFT|RSHIFT)?\s*(?P<Y>\w+)?\s*->\s*(?P<Z>\w+)?$
    """, re.VERBOSE)

    operations = {}
    for line in load_input(day=7).readlines():
        match = re.match(pattern, line)
        if match:
            op = match.group('op')
            X = match.group('X')
            Y = match.group('Y')
            Z = match.group('Z')
            operations[Z] = [
                coalesce(op, 'ASSIGN'),
                coalesce(X, Y),
                Y if X else None
            ]
    
    return operations


def resolve(wire, operations={}):
    '''Recursively resolves wires'''

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
    '''Given the input operations, returns the signal ultimately provided to wire a'''
    a = ctypes.c_uint16(resolve('a', create_input()))
    return a.value
    

def part2():
    '''Injects original value of a into wire b and resolves wire a again'''

    # resolves wire a
    operations = create_input()
    a = ctypes.c_uint16(resolve('a', operations))

    # overwrites wire b with the value of wire a
    operations['b'] = ['ASSIGN', a.value, None]

    # resolves wire a again
    a = ctypes.c_uint16(resolve('a', operations))

    return a.value


if __name__ == '__main__':
    print(part1())
    print(part2())