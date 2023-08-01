import re
from collections import defaultdict
from itertools import permutations
from typing import Dict, List, Tuple

from helper import load_input


def create_input():
    '''Extract puzzle input'''
    return [line.strip() for line in load_input(day=15).readlines()]


def parse_input(lines: List[str]) -> Dict[str, Dict]:
    '''
    Extracts ingredient names and properties from input (lines), 
    storing results in a combined dictionary
    ''' 
    pattern = re.compile(
        r'(?P<name>\w+).+?'
        r'(?P<capacity>-?\d+).+?'
        r'(?P<durability>-?\d+).+?'
        r'(?P<flavor>-?\d+).+?'
        r'(?P<texture>-?\d+).+?'
        r'(?P<calories>-?\d+)'
    )

    ingredients = {}

    for line in lines:

        match = re.match(pattern, line)

        if match:
            ingredients[match.group('name')] = {
                k: int(v) for k, v in match.groupdict().items() 
                if v.isdigit() or v.startswith("-")
            }

    return ingredients


def part1():
    ...    


def part2():
    ...


if __name__ == '__main__':
    print(part1())
    print(part2())