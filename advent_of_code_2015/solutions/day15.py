import re
from collections import defaultdict
from itertools import product, starmap
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

    # swap ingredients and properties to create alternative view
    properties = {}
    for k, v in ingredients.items():
        for k2, v2 in v.items():
            properties.setdefault(k2, {})[k] = v2

    return ingredients, properties


def part1():

    ingredients, properties = parse_input(create_input())

    # preset ingredient ranges
    valid_teaspoons = {i: set(range(1, 98)) for i in ingredients}

    scores = defaultdict(set)

    # extract each property at a time
    for prop, v in properties.items():

        if prop == 'calories':
            continue
    
        code = ''
        active = {}
        for ingredient, prop_per_teaspoon in v.items():

            if prop_per_teaspoon == 0:
                continue

            else:
                active[ingredient] = 0  # placeholder
                code += f'+{prop_per_teaspoon}*active["{ingredient}"]'
            
        code = compile(code, f'<eval-{prop}>', 'eval')

        list_of_active = list(active.keys())

        orig_valid_teaspoons = valid_teaspoons.copy()

        for ingredient in list_of_active:
            valid_teaspoons[ingredient] = set([1])

        for prod in product(*[orig_valid_teaspoons[s] for s in list_of_active]):

            if sum(prod) > 100:
                continue

            for i, ingredient in enumerate(list_of_active):
                active[ingredient] = prod[i]

            eval_result = eval(code)
            if eval_result > 0:
                for ingredient in list_of_active:
                    valid_teaspoons[ingredient].add(active[ingredient])
                scores[prop].add(eval_result)


    # find maximum

    code = []
    active = {}

    for prop, v in properties.items():

        active_code = ''

        if prop == 'calories':
            continue
    
        for ingredient, prop_per_teaspoon in v.items():

            active[ingredient] = 0  # placeholder

            if prop_per_teaspoon == 0:
                continue

            else:
                active_code += f'+{prop_per_teaspoon}*active["{ingredient}"]'
        
        code.append(f'({active_code})')

    code = compile('*'.join(code), f'<eval-all>', 'eval')

    mx = 1
    for prod in product(*[valid_teaspoons[s] for s in valid_teaspoons.keys()]):
        if sum(prod) > 100:
            continue

        for i, ingredient in enumerate(valid_teaspoons.keys()):
            active[ingredient] = prod[i]

        eval_result = eval(code)
        if eval_result > mx:
            mx = eval_result

    return mx


def part2():
    ...


if __name__ == '__main__':
    print(part1())
    print(part2())