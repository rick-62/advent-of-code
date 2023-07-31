import re
from collections import defaultdict
from itertools import permutations
from typing import Dict, List, Tuple

from helper import load_input


def create_input():
    '''Extract puzzle input'''
    return [line.strip() for line in load_input(day=14).readlines()]


def parse_input(lines: List[str]) -> Dict[str, Dict]:
    '''
    Extracts reindeers and all values from input returning dictionary,
    using their names as dictionary keys and the value being the dictionary of values.
    ''' 
    pattern = r'^(?P<name>\w+).+?(?P<v>\d+).+?(?P<t1>\d+).+?(?P<t2>\d+)'

    reindeers = {}

    for line in lines:

        match = re.match(pattern, line)

        if match:
            reindeers[match.group('name')] = {
                k: int(v) for k, v in match.groupdict().items() if v.isdigit()
            }
            # example - {Comet: {v: 14, t1: 10, t2: 127}}

    return reindeers


def distance_travelled(t, v=None, t1=None, t2=None, **kwargs):
    '''
    Given total time t, velocity v, flying time t1 & rest time t1
    calculates the total distance travelled
    '''
    return (

        # distance travelled over complete cycles
        v * t1 * int(t / (t1 + t2)) +

        # additional distance travelled over incomplete cycle
        v * min(t1, t - (t1 + t2) * int(t / (t1 + t2)))
    )


def score_reindeer(reindeers: Dict[str, Dict], t=1) -> Dict[str, int]:
    '''
    given parsed reindeers data and total time t, 
    calculates total score for each reindeer based on who is in the lead after each second.
    (If there are multiple reindeer tied for the lead, they each get one point.)
    returns dictionary of reindeers & points.
    '''
    points = defaultdict(int)

    # cycles through each second
    for i in range(1, t+1):

        mx = (0, [])  # stores current leaders (distance and list of names)

        for name, obj in reindeers.items():
            d = distance_travelled(i, **obj)

            # replace maximum with new leader and distance
            if d > mx[0]:
                mx = (d, [name])

            # adds leader where winning distance equals
            elif d == mx[0]:
                mx[1].append(name)

        # adds up points for each reindeer within this iteration
        for name in mx[1]:
            points[name] += 1

    return points

            
def part1(t=2503):
    '''after exactly 2503 seconds, what distance has the winning reindeer traveled'''
    mx = 0
    for obj in parse_input(create_input()).values():
        d = distance_travelled(t, **obj)
        
        mx = max(mx, d)
    
    return mx       


def part2(t=2503):
    '''
    New scoring system. At the end of each second, 
    one point is awarded to the reindeer currently in the lead. 
    returns total points of winning reindeer
    '''
    reindeers = parse_input(create_input())
    return max(score_reindeer(reindeers, t=t).values())


if __name__ == '__main__':
    print(part1())
    print(part2())