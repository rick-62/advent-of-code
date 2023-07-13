import re
from helper import load_input
from dataclasses import dataclass

@dataclass
class String:
    s: str

    ## PART 1 ##

    def contains_three_vowels(self):
        return len(re.findall(r'[aeiou]', self.s)) >= 3

    def has_repeated_letter(self):
        for i in range(len(self.s) - 1):
            if self.s[i] == self.s[i + 1]:
                return True
        return False
    
    def no_forbidden_substrings(self):
        if 'ab' in self.s: return False
        if 'cd' in self.s: return False
        if 'pq' in self.s: return False
        if 'xy' in self.s: return False
        else: return True

    def naughty_or_nice(self):
        return all([
            self.contains_three_vowels(),
            self.has_repeated_letter(),
            self.no_forbidden_substrings()
        ])

    ## PART 2 ##

    def contains_repeating_pair(self):
        '''
        contains a pair of any two letters that appears at least twice in the string
        without overlapping
        '''
        if len(self.s) < 4:
            return False

        for i in range(0, len(self.s) - 2):
            pair = self.s[i:i+2]
            if pair in self.s[i+2:]:
                return True
        else:
            return False

    def contains_repeated_letter(self):
        '''contains at least one letter which repeats with exactly one letter between them'''
        if len(self.s) < 3:
            return False

        for i in range(0, len(self.s) - 2):
            if self.s[i] == self.s[i+2]:
                return True
        else:
            return False



def create_input():
    '''read in puzzle input from file and convert to Present objects'''
    return load_input(day=5).readlines()


def part1():
    '''count the number of nice strings'''
    strings = [String(s).naughty_or_nice() for s in create_input()]
    return sum(strings)

def part2():
    '''count the number of nice strings, based on new parameters'''
    total = 0
    for string in create_input():
        s = String(string)
        if s.contains_repeating_pair() and s.contains_repeated_letter():
            total += 1
    return total


if __name__ == '__main__':
    print(part1())
    print(part2())