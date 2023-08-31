import re
from collections import Counter, defaultdict
from itertools import combinations
from typing import Dict, List, Tuple, Set

import numpy as np
from helper import load_input


def create_input():
    '''Extract puzzle input and transform'''

    # creates pattern for extracting replcements
    pattern = r"(\w+) => (\w+)"

    # splits puzzle input into replacements and molecule
    replacements, molecule = load_input(day=19).read().strip("\n").split("\n\n")

    # regex and init empty dict of lists
    matches = re.findall(pattern, replacements)
    replacements_dict = defaultdict(list)

    # converts the replacements into dictionary of lists
    for match in matches:
        replacements_dict[match[0]].append(match[1])

    return replacements_dict, molecule


def insert_replacements(start: str, end: str, replacements: List[str]) -> List[str]:
    '''
    Given start & end of molecule and a list of replacements,
    incrementally inserts replacements between start and end to create new molecules.
    Returns this as a list.
    '''
    return [
        start + replacement + end 
        for replacement in replacements
    ]
 

def generate_molecules(replacements_dict: Dict[str, List[str]], molecule: str) -> Set[str]:
    '''
    Given the replacements and starting molecule, 
    generates all the possible molecules after replacement,
    and returns as a set.
    '''

    # Prep storage for generated molecules
    generated_molecules = set()

    # loop through each element in starting molecule
    for i, element in enumerate(molecule):

        # extract replacements if a match
        replacement1 = replacements_dict.get(element, None)
        replacement2 = replacements_dict.get(molecule[i:i+2], None)

        # slice the correct end of molecule, dependent on length
        if replacement1:
            end = molecule[i+1:]
        elif replacement2:
            end = molecule[i+2:] 
        else:
            continue
        
        # Updates the generated molecules set with new molecules after replacement
        generated_molecules.update(insert_replacements(
                start = molecule[:i], 
                end = end, 
                replacements = replacement1 or replacement2)
        )

    return generated_molecules


def part1():
    '''
    How many distinct molecules can be created 
    after all the different ways you can do one replacement on the medicine molecule
    '''
    replacements_dict, molecule = create_input()
    return len(generate_molecules(replacements_dict, molecule))

def part2():
    ...


if __name__ == '__main__':
    print(part1())
    print(part2())