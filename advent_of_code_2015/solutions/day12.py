import json
import re

from helper import load_input


def create_input():
    '''Extract puzzle input'''
    return load_input(day=12).read()


def sum_digits(text: str):
    '''Extracts and sums all the digits from a string of text'''
    digits = re.findall(r'-?\d+', text)
    return sum([int(d) for d in digits])


def find_red(obj: dict):
    '''traverses json dictionary to identify all objects containing the property red'''

    results = []

    if isinstance(obj, dict):

        # if contains value of red in dict object, returns object
        if "red" in obj.values():
            results.append(obj)

        # else loops through all object values to find_red
        else:
            for value in obj.values():
                results.extend(find_red(value))

    # for lists we loop through items to find_red
    elif isinstance(obj, list):
            for item in obj:
                results.extend(find_red(item))
    
    # finally removing any empty & null value and returning the results
    return [red for red in results if red]


def sum_digits_where_red(text: str):
    '''
    Extracts and sums all the digits from a string of text, 
    but only where the digit has any property with the value "red".
    This only for objects ({...}), not arrays ([...]).
    '''

    # converts text to json
    data = json.loads(text)

    # returns list of all objects (& children) containing property "red" 
    results = find_red(data)

    # converts list of objects to string and sums digits
    return sum_digits(str(results))


def part1():
    '''sum all the digits from the puzzle input'''
    return sum_digits(create_input())


def part2():
    '''sum all the digits from the puzzle input minus those in red objects'''
    return part1() - sum_digits_where_red(create_input())


if __name__ == '__main__':
    print(part1())
    print(part2())