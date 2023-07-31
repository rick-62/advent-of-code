import re
from collections import defaultdict
from itertools import permutations
from typing import Dict, List, Tuple

from helper import load_input


def create_input():
    '''Extract puzzle input'''
    return [line.strip() for line in load_input(day=13).readlines()]


def parse_input(lines: List[str]) -> Dict[Tuple[str, str], int]:
    '''
    Extracts names and happiness scores from input list, 
    creating dictionary of name pairs and net happiness units.
    ''' 

    pattern = r'^(?P<name1>\w+).+(?P<gain_or_lose>gain|lose) (?P<units>\d+).+\s(?P<name2>\w+).$'

    weights = defaultdict(int)
    names = set()

    for line in lines:

        match = re.match(pattern, line)

        if match:
            name_pair = tuple(sorted([match.group('name1'), match.group('name2')]))
            units = int(match.group('units'))
            if match.group('gain_or_lose') == 'lose':
                units *= -1

            weights[name_pair] += units
            names.add(match.group('name1'))
            names.add(match.group('name2'))

    return names, weights


def find_optimal_seating_arrangement(names: set, weights: Dict) -> Tuple[int, str]:
    '''
    naive solution:
        - for all permutations of names
        - extracts all pairs of guests
        - for each pair gets total happiness units from weights
    
    returns optimal score and optimal arrangement.
    '''

    length = len(names)

    optimal = (0, None)

    for perm in permutations(names):

        score = 0
        for i in range(length):
            pair = perm[i], perm[(i+1)%length]
            score += weights.get(tuple(sorted(pair)), 0)

        if score > optimal[0]:
            optimal = (score, perm)

    return optimal

            
def part1():
    '''
    What is the total change in happiness for the optimal seating arrangement 
    of the actual guest list?
    '''
    names, weights = parse_input(create_input())
    score, _ = find_optimal_seating_arrangement(names, weights)
    return score


def part2():
    '''
    What is the total change in happiness for the optimal seating arrangement 
    of the guest list, including you 
    '''
    names, weights = parse_input(create_input())
    names.add('Me')
    score, _ = find_optimal_seating_arrangement(names, weights)
    return score


if __name__ == '__main__':
    print(part1())
    print(part2())