import re
from dataclasses import dataclass

from helper import load_input


class String:
    literal: str
    memory: str

    


@dataclass
def create_input():
    '''Extract puzzle input'''
    return load_input(day=8).readlines()






def part1():
    ''''''
    pass
    

def part2():
    ''''''
    pass


if __name__ == '__main__':
    print(part1())
    print(part2())