import re
from collections import defaultdict
from typing import Dict, List, Tuple

import numpy as np
from helper import load_input


def create_input():
    '''Extract puzzle input'''
    return [line.strip() for line in load_input(day=15).readlines()]


def parse_input(lines: List[str]) -> Dict[str, Dict]:
    '''
    Extracts properties from input (lines), returning 2D numpy array.
    Each row is in relation to each property. 
    Each column is in relation to each ingredient.
    Index of properties/ingredients matches order they appear in input.
    ''' 
    properties = []

    for line in lines:
        values = re.findall(r'-?\d+', line)
        properties.append([int(v) for v in values])

    return np.vstack(properties).T


def yield_teaspoon_combinations_for_four_ingredients(max_teaspoons=100):
    '''loop through possible combinations whose sum does not exceed max_teaspoons'''
    for i in range(max_teaspoons + 1):
        for j in range(max_teaspoons + 1 - i):
            for k in range(max_teaspoons + 1 - i - j):
                l = max_teaspoons - i - j - k
                yield np.array([i, j, k, l])


def calculate_score(teaspoons, properties):
    '''given teaspoon combination, calculates the score'''
    arr1 = np.matmul(properties, teaspoons)
    arr2 = np.where(arr1 < 0, 0, arr1)
    arr3 = np.prod(arr2)
    return arr3


def part1():
    '''calculate the max score, excluding calories property'''

    # parse input
    properties = parse_input(create_input())

    # remove last row (calories)
    properties = properties[:-1]

    # calculate max score
    return max([
        calculate_score(teaspoons, properties) 
        for teaspoons in  yield_teaspoon_combinations_for_four_ingredients()
    ])


def part2():
    '''calculate the max score, where calorie sum equals 500'''

    # parse input
    properties = parse_input(create_input())

    # extract calories
    calories = properties[-1]

    # remove last row
    properties = properties[:-1]

    # calculate max score, excluding where calories score != 500
    return max([
        calculate_score(teaspoons, properties) 
        for teaspoons in  yield_teaspoon_combinations_for_four_ingredients()
        if calculate_score(teaspoons, calories) == 500
    ])


if __name__ == '__main__':
    print(part1())
    print(part2())