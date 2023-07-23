import os

def load_input(day, encoding="ascii"):
    '''load pre-downloaded puzzle input for specified day'''

    return open(
        os.path.join('advent_of_code_2015', 'inputs', f'day{day:0>2}.txt'), 
        encoding=encoding
    )

def coalesce(*args):
    '''coalesce list of arguments'''
    for arg in args:
        if arg is not None:
            return arg
