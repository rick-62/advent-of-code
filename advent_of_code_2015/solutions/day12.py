import re

from helper import load_input


def create_input():
    '''Extract puzzle input'''
    return load_input(day=12).read()


def sum_digits(text: str):
    '''Extracts and sums all the digits from a string of text'''
    digits = re.findall(r'-?\d+', text)
    return sum([int(d) for d in digits])


def sum_digits_where_red(text: str):
    '''
    Extracts and sums all the digits from a string of text, 
    but only where the digit has any property with the value "red".
    This only for objects ({...}), not arrays ([...]).
    '''
    red_objects = re.findall(r'{[^{]*:"red"[^}]*}', text)

    total = 0
    for obj in red_objects:
        total += sum_digits(obj)

    return total


def part1():
    '''sum all the digits from the puzzle input'''
    return sum_digits(create_input())


def part2():
    '''sum all the digits from the puzzle input minus those in red objects'''
    return part1() - sum_digits_where_red(create_input())


if __name__ == '__main__':
    print(part1())
    print(part2())