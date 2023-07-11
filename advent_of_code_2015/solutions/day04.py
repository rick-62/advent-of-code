import hashlib
from itertools import count

from helper import load_input


def create_input():
    '''read in puzzle input from file and convert to Present objects'''
    return load_input(day=4).read().strip()

def get_md5_hash(string):
    '''
    given a string, returns the hash value of an object 
    as a string of hexadecimal digits.
    ''' 
    hash_object = hashlib.md5(string.encode())
    return hash_object.hexdigest()

def find_decimal_suffix_of_string(string, zeros='00000'):
    '''
    given a string, find the first decimal suffix 
    which results in a md5 hash beginning with five zeroes 
    '''
    for i in count(1):
        if get_md5_hash(string + str(i)).startswith(zeros):
            return i

def part1():
    '''find MD5 hash which, in hexadecimal, start with at least five zeroes'''
    return find_decimal_suffix_of_string(create_input())

def part2():
    '''find MD5 hash which, in hexadecimal, start with at least six zeroes'''
    return find_decimal_suffix_of_string(create_input(), zeros='000000')


if __name__ == '__main__':
    print(part1())
    print(part2())