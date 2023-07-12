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
        pass



def create_input():
    '''read in puzzle input from file and convert to Present objects'''
    return load_input(day=5).readlines()


def part1():
    '''count the number of nice strings'''
    strings = [String(s).naughty_or_nice() for s in create_input()]
    return sum(strings)

def part2():
    pass


if __name__ == '__main__':
    print(part1())
    print(part2())