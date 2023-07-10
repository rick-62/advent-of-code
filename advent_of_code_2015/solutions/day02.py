
from dataclasses import dataclass

from helper import load_input


@dataclass
class Present:
    l: int
    w: int
    h: int

    def calculate_surface_area(self):
        l, w, h = self.l, self.w, self.h
        return 2*l*w + 2*w*h + 2*h*l

    def calculate_area_of_smallest_side(self):
        l, w, h = self.l, self.w, self.h
        return min(l*h, l*w, w*h)

    def calculate_length_of_ribbon_for_present(self):
        '''
        The ribbon required to wrap a present is the shortest distance around its sides, 
        or the smallest perimeter of any one face.
        '''
        dim = sorted([self.l, self.w, self.h])
        return dim[0] * 2 + dim[1] * 2
        
    def calculate_length_of_ribbon_for_bow(self):
        '''
        the feet of ribbon required for the perfect bow is equal to 
        the cubic feet of volume of the present.
        '''
        return self.l * self.w * self.h

    
def create_input():
    '''read in puzzle input from file and convert to Present objects'''
    dims = [line.split('x') for line in load_input(day=2).readlines()]
    return [Present(l=int(dim[0]), w=int(dim[1]), h=int(dim[2])) for dim in dims]

def part1():
    '''How many total square feet of wrapping paper required.'''
    presents = create_input()
    total = 0
    for p in presents:
        total += p.calculate_surface_area()
        total += p.calculate_area_of_smallest_side()
    return total

def part2():
    '''How many total feet of ribbon required.'''
    presents = create_input()
    total = 0
    for p in presents:
        total += p.calculate_length_of_ribbon_for_present()
        total += p.calculate_length_of_ribbon_for_bow()
    return total

if __name__ == '__main__':
    print(part1())
    print(part2())