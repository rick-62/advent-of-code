import re

from helper import load_input


def create_input():
    '''Extract puzzle input'''
    return load_input(day=11).read().strip('\n')


def is_valid_password(string):
    '''
    Checks validity of password, returning True/False.

    Validity checks:
    1. increasing straight of at least three letters
    2. two different, non-overlapping pairs
    '''

    # Passwords must include one increasing straight of at least three letters
    straight = 0
    for i in range(len(string) - 2):
        if ord(string[i]) == ord(string[i+1]) - 1 == ord(string[i+2]) - 2:
            straight += 1
            break
    if straight == 0:
        return False

    # Passwords must contain at least two different, non-overlapping pairs
    pattern = r'(\w)\1(?!.*\1\1).*?(\w)\2(?!.*\2\2)'
    if not bool(re.search(pattern, string)):
        return False

    return True


def get_next_password(old_password):
    '''Given the old password, increments through valid passwords, yielding the next'''

    chars = "abcdefghjkmnopqrstuvwxyz"  # non-valid characters i, l and o have been removed

    # converts the old password if contains any non-valid characters
    for i, char in enumerate(old_password):
        if char in 'iol':
            old_password = (
                old_password[:i] + 
                chr(ord(old_password[i]) + 1) + 
                'a'*len(old_password[i+1:])
            )
            break


    def increment_string(string):
        '''Yields incremented string, based on chars'''

        while True:

            # loops through the string index in reverse (7 -> 0)
            for i in range(len(string)-1, -1, -1):

                # if character is 'z' then resets to 'a' and loops to next element in list
                if string[i] == 'z':
                    string = string[:i] + 'a' + string[i+1:]
                
                # if character not 'z' then increments to the next character and breaks loop
                else:
                    string = string[:i] + chars[chars.find(string[i]) + 1] + string[i+1:]
                    break
            
            yield string


    # loops through strings and yields result if valid
    for string in increment_string(old_password):
        if is_valid_password(string):
            yield string


def part1():
    '''
    Santa's previous password expired, and he needs help choosing the next one. 
    He finds his new password by incrementing his old password string repeatedly until it is valid.
        # passwords must be exactly eight lowercase letters
        # Passwords must include one increasing straight of at least three letters
        # Passwords may not contain the letters i, o, or l
        # Passwords must contain at least two different, non-overlapping pairs
    '''
    old_password = create_input()
    pw = get_next_password(old_password)
    return next(pw)


def part2():
    '''Simply yields the next valid password after part 1'''
    return next(get_next_password(part1()))


if __name__ == '__main__':
    print(part1())
    print(part2())