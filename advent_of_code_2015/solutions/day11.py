import re

from helper import load_input


def create_input():
    '''Extract puzzle input'''
    return load_input(day=11).read().strip('\n')


def is_valid_password(string):

    # passwords must be exactly eight lowercase letters
    if len(string) != 8:
        return False

    # Passwords may not contain the letters i, o, or l
    if 'i' in string or 'o' in string or 'l' in string:
        return False

    # Passwords must include one increasing straight of at least three letters
    straight = 0
    for i in range(len(string) - 2):
        if ord(string[i]) == ord(string[i+1]) - 1 == ord(string[i+2]) - 2:
            straight += 1
    if straight == 0:
        return False

    # Passwords must contain at least two different, non-overlapping pairs
    pattern = r'(\w)\1(?!.*\1\1).*?(\w)\2(?!.*\2\2)'
    if not bool(re.search(pattern, string)):
        return False

    return True


def part1():
    '''
    Santa's previous password expired, and he needs help choosing a new one. 
    He finds his new password by incrementing his old password string repeatedly until it is valid.
    # passwords must be exactly eight lowercase letters
    # Passwords must include one increasing straight of at least three letters
    # Passwords may not contain the letters i, o, or l
    # Passwords must contain at least two different, non-overlapping pairs
    '''

    # tempted to remake thsi using numpy
    # convert letters to ord eqivilent?
    # Or not and jst need to increment through passwords

def part2():
    ...


if __name__ == '__main__':
    print(part1())
    print(part2())