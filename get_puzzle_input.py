import requests
import os
import sys


def download_puzzle_input(day, year):
    '''download the users puzzle input from Advent of Code site'''

    cookies = {'session': os.getenv('session')}

    r = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies=cookies)

    r.raise_for_status()

    return r


def save_puzzle_input(text, day, year):
    '''save puzzle input as text file'''

    with open(f'advent_of_code_{year}/inputs/day{day:0>2}.txt', 'w') as f:
        f.write(text)
    

if __name__ == '__main__':

    day, year = int(sys.argv[1]), int(sys.argv[2])
    
    r = download_puzzle_input(day, year)
    save_puzzle_input(r.text, day, year)