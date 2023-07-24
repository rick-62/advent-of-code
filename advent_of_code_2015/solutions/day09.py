import re
from itertools import permutations
from operator import gt, lt

import networkx as nx
from helper import load_input


def create_input():
    '''Extract puzzle input'''
    return load_input(day=9).readlines()


def create_network(connections):
    '''converts input into network optimised structure'''
    G = nx.Graph()
    pattern = r"(\w+) to (\w+) = (\d+)"
    for line in connections:
        match = re.search(pattern, line)
        G.add_edge(
            match.group(1),                 # from
            match.group(2),                 # to
            weight=int(match.group(3))      # distance
        )
    return G


def traveling_santa_problem(graph: nx.Graph, op=lt):
    '''
    given graph of all connections & distances and comparison operator,
    finds the optimal path and distance
    '''
    optimal_distance = None
    optimal_route = None
    for route in permutations(graph.nodes()):
        distance = sum([graph[a][b]['weight'] for a, b in zip(route[:-1], route[1:])])
        if optimal_distance is None or op(distance, optimal_distance):
            optimal_distance = distance
            optimal_route = route
    return optimal_route, optimal_distance


def part1():
    '''find route with shortest distance'''
    connections = create_input()
    graph = create_network(connections)
    route, distance = traveling_santa_problem(graph)
    return distance
    

def part2():
    '''find route with longest distance'''
    connections = create_input()
    graph = create_network(connections)
    route, distance = traveling_santa_problem(graph, op=gt)
    return distance


if __name__ == '__main__':
    print(part1())
    print(part2())