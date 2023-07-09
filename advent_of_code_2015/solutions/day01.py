
from helper import load_input 

def create_input():
    '''read in puzzle input from file'''
    return load_input(day=1).read()

def find_final_floor(directions: str):
    '''given directions find final floor'''
    return directions.count('(') - directions.count(')')

def first_enters_basement(directions: str):
    '''given directions find first point at which enters basement'''
    floor = 0
    for i, d in enumerate(directions, 1):
        if d == '(':
            floor += 1
        elif d == ')':
            floor -= 1
        else:
            pass
        if floor == -1:
            return i

def part1():
    directions = create_input()
    return find_final_floor(directions)

def part2():
    directions = create_input()
    return first_enters_basement(directions)

if __name__ == '__main__':
    print(part1())
    print(part2())

