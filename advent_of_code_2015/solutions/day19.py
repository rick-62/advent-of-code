import re
from collections import Counter, defaultdict
from itertools import combinations
from typing import Dict, List, Tuple

import numpy as np
from helper import load_input


def create_input():
    '''Extract puzzle input'''

    arr = np.genfromtxt(load_input(day=19), dtype=str, delimiter=1, comments=None)

    return arr



def part1():
    ...


def part2():
    ...


if __name__ == '__main__':
    print(part1())
    print(part2())