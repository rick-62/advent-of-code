from collections import defaultdict

from helper import load_input


def create_input():
    '''read in puzzle input from file and convert to Present objects'''
    return load_input(day=3).read()

def log_visited_houses(movements):
    '''Converts input into a dictionary of visited locations/coordinates'''
    log = defaultdict(complex)
    DIR = {'^': 1j, '<': -1, '>': 1, 'v': -1j}

    log[0+0j] = 1
    last_visited = 0+0j
    for x in movements:
        last_visited += DIR[x]
        log[last_visited] += 1
    return log

def unzip_movements_into_two(movements):
    movements1, movements2 = zip(*[
        (movements[i], movements[i+1]) for i in range(0, len(movements), 2)
    ])
    return movements1, movements2

def count_visited_houses(*logs):
    '''given any number of logs are arguments, counts distinct keys'''
    dct = {}
    for log in logs:
        dct.update(log)
    return len(dct)

def part1():
    '''how many houses receive at least one present'''
    movements = create_input()
    log = log_visited_houses(movements)
    return count_visited_houses(log)

def part2():
    '''how many houses receive at least one present, with additional robot'''
    movements = create_input()
    movements1, movements2 = unzip_movements_into_two(movements)
    log1 = log_visited_houses(movements1)
    log2 = log_visited_houses(movements2)
    return count_visited_houses(log1, log2)

if __name__ == '__main__':
    print(part1())
    print(part2())