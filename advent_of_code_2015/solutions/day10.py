from itertools import groupby

from helper import load_input


def create_input():
    '''Extract puzzle input'''
    return load_input(day=10).read().strip('\n')


def solve_next_sequence(digits):
    '''
    Given a list or string of ordered digits, returns the next pattern in the sequence.
        1 becomes 11
        11 becomes 21
        21 becomes 1211
        1211 becomes 111221
        111221 becomes 312211
    '''
    return ''.join([                # combines list into string
        str(len(list(group))) + key # gets length of group as string and appends to key 
        for key, group              # key = grouped digit; group = digits in group   
        in groupby(digits)          # groups digits
    ])


def part1():
    '''Given puzzle input find the length of the sequence after 40 iterations'''
    digits = create_input()
    for _ in range(40):
        digits = solve_next_sequence(digits)
    return len(digits)
    

def part2():
    '''Given puzzle input find the length of the sequence after 50 iterations'''
    digits = create_input()
    for _ in range(50):
        digits = solve_next_sequence(digits)
    return len(digits)


if __name__ == '__main__':
    print(part1())
    print(part2())