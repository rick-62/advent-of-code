import re

from helper import load_input


def evaluate_string(s):
    '''
    Replaces relevant escape sequences with #, 
    and removes surrounding quotes
    '''
    s = s.replace(r'\\', '#')
    s = s.replace(r'\"', '#')
    s = re.sub(r'\\x[0-9a-fA-F][0-9a-fA-F]', '#', s)
    s = s.strip('"')
    return s

def encode_string(s):
    '''
    Encodes relevant escape sequences with additional #,
    and adds surrounding quotes
    '''
    s = re.sub(r'\\x[0-9a-fA-F][0-9a-fA-F]', '#####', s)
    s = s.replace('\\', '##')
    s = s.replace('"', '#"')
    s = '"' + s + '"'
    return s


def create_input():
    '''Extract puzzle input'''
    return load_input(day=8).read().splitlines()


def part1():
    '''
    returns the total length of string literals minus length of string in memory,
    given the puzzle input list of coded strings
    '''
    sum_literals = 0
    sum_memory = 0
    for literal in create_input():
        sum_literals += len(literal)
        sum_memory += len(evaluate_string(literal))
    return sum_literals - sum_memory
    

def part2():
    '''
    returns the total length of the encoded string minus 
    the total length of the original string literals
    '''
    sum_literals = 0
    sum_encoded = 0
    for literal in create_input():
        sum_literals += len(literal)
        sum_encoded += len(encode_string(literal))
    return sum_encoded - sum_literals


if __name__ == '__main__':
    print(part1())
    print(part2())