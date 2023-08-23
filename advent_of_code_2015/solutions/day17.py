import re
from collections import Counter, defaultdict
from itertools import combinations
from typing import Dict, List, Tuple

import numpy as np
from helper import load_input


def create_input():
    '''Extract puzzle input'''
    return [
        int(line.strip()) 
        for line in load_input(day=17).read().split('\n') 
        if line.strip() != ''
    ]


def valid_combinations(containers: List[int], eggnog=150):
    '''
    Given the parsed puzzle input (containers) and amount of eggnog to store, 
    yields valid combinations of containers to store the eggnog
    ''' 
    for i in range(2, len(containers)):
        for combo in combinations(containers, i):
            if sum(combo) == eggnog:
                yield combo


def part1():
    '''Find how many different combinations of containers to store eggnog'''
    return len(list(valid_combinations(create_input())))


def part2():
    '''
    Find how many different combinations of containers to store eggnog,
    but by only using minimum number of containers
    '''
    counter = Counter(len(combo) for combo in valid_combinations(create_input()))
    return min(counter.items())[1]


if __name__ == '__main__':
    print(part1())
    print(part2())