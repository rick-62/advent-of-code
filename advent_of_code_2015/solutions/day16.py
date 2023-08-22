import re
from collections import defaultdict
from typing import Dict, List, Tuple

import numpy as np
from helper import load_input

TAPE = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}


def create_input():
    '''Extract puzzle input'''
    return [line.strip() for line in load_input(day=16).readlines()]


def parse_input(gift_list: List[str]) -> List[Dict[str, int]]:
    '''Converts input into list of dictionaries containing gift quantity key-value pairs'''
    
    pattern = r"(\w+): (\d+),? ?"

    return [
        {k: int(v) for k, v in re.findall(pattern, gifts)} 
        for gifts in gift_list
    ]


def part1():
    '''Finds the correct Aunt Sue by checking for subsets of gifts'''
    gift_list = parse_input(create_input())

    for sue, gifts in enumerate(gift_list, start=1):
        if gifts.items() <= TAPE.items():
            return sue 


def part2():
    '''
    Finds the correct Aunt Sue, with more thorough checking than Part 1:
    - cats and trees readings indicates that there are greater than that many 
    - pomeranians and goldfish readings indicate that there are fewer than that many
    '''
    gift_list = parse_input(create_input())

    for sue, gifts in enumerate(gift_list, start=1):

        check = []

        for gift, amount in gifts.items():

            if gift in ['cats', 'trees']:
                check.append(amount > TAPE[gift])

            elif gift in ['pomeranians', 'goldfish']:
                check.append(amount < TAPE[gift])

            else:
                check.append(TAPE[gift] == amount)

        if all(check):  
            return sue


if __name__ == '__main__':
    print(part1())
    print(part2())