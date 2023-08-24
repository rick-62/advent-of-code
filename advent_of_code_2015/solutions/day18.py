import re
from collections import Counter, defaultdict
from itertools import combinations
from typing import Dict, List, Tuple

import numpy as np
from helper import load_input


def create_input():
    '''Extract puzzle input'''
    return np.genfromtxt(load_input(day=18), dtype=str, delimiter=1, comments=None)


def part1():
    '''
    In your grid of 100x100 lights, given your initial configuration, 
    how many lights are on after 100 steps?
    '''
    return create_input()


def part2():
    
    ...


if __name__ == '__main__':
    print(part1())
    print(part2())