import re
from collections import Counter, defaultdict
from itertools import combinations
from typing import Dict, List, Tuple

import numpy as np
from helper import load_input


def create_input():
    '''Extract puzzle input'''

    # loads puzzle input as numpy array of '#' and '.'
    arr = np.genfromtxt(load_input(day=18), dtype=str, delimiter=1, comments=None)

    # vectorise function to convert the array to 1s and 0s
    fn = np.vectorize(lambda x: 1 if x == '#' else 0)

    # applies function and returns new array
    return fn(arr)


def animate_lights(arr: np.array) -> np.array:
    import numpy as np

    # Pad the array with zeros
    padded = np.pad(arr, pad_width=1, mode='constant', constant_values=0)

    # Define the window size
    window_size = 3

    # Create an empty array to store the results
    result = np.zeros_like(arr)

    # Loop through the array
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            # Get the 3x3 window around the current element
            window = padded[i:i+window_size, j:j+window_size]
            # Sum the window elements and subtract the current element
            neighbors = np.sum(window) - arr[i,j]
            # Light remains on if number of lit neighbors is 2 or 3
            if arr[i,j] == 1 and neighbors in [2, 3]:
                result[i,j] = 1
            # Light turns on if number of lit neighbors is exactly 3
            elif arr[i,j] == 0 and neighbors == 3:
                result[i,j] = 1

    # Returns the result
    return result


def part1():
    '''
    In your grid of 100x100 lights, given your initial configuration, 
    how many lights are on after 100 steps?
    '''
    arr = create_input()
    for i in range(100):
        arr = animate_lights(arr)

    return np.sum(arr)

def part2():
    
    ...


if __name__ == '__main__':
    print(part1())
    print(part2())