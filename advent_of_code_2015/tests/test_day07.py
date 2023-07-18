from collections import namedtuple
from unittest.mock import mock_open, patch

import pytest
from solutions import day07


def test_lookup():
    assert day07.LOOKUP['AND'](1,1) == 1
    assert day07.LOOKUP['OR'](0,1) == 1
    assert day07.LOOKUP['LSHIFT'](1,1) == 2
    assert day07.LOOKUP['NOT'](1) == -2
    assert day07.LOOKUP['NOT'](66000) == -66001
    assert day07.LOOKUP['ASSIGN'](10) == 10


@pytest.mark.parametrize(
    's, op, X, Y, Z', [
        ('123 -> x', 'ASSIGN', '123', None, 'x'),  
        ('456 -> y', 'ASSIGN', '456', None, 'y'),  
        ('x AND y -> d', 'AND', 'x', 'y', 'd'),  
        ('x OR y -> e', 'OR', 'x', 'y', 'e'),  
        ('x LSHIFT 2 -> f', 'LSHIFT', 'x', '2', 'f'),  
        ('y RSHIFT 2 -> g', 'RSHIFT', 'y', '2', 'g'),  
        ('NOT x -> h', 'NOT', 'x', None, 'h'),  
        ('NOT y -> i', 'NOT', 'y', None, 'i'),  
    ]
)
def test_create_input(s, op, X, Y, Z):
    with patch('builtins.open', mock_open(read_data=s)):
        returns = day07.create_input()
        assert returns[Z] == [op, X, Y]


def test_resolve():

    assert day07.resolve(123) == 123
    assert day07.resolve('123') == 123

    # basic operation
    day07.operations={
        'a': ['AND', 1, 2]
    }
    assert day07.resolve('a') == 0

    # recurse
    day07.operations={
        'a': ['AND', '1', 'b'],
        'b': ['LSHIFT', '1', '1'],
    }
    assert day07.resolve('a') == 0

    # NOT operation - perk of pytest causing issues
    del day07.operations
    day07.operations={
        'a': ['NOT', '7', None],
    }
    assert day07.resolve('a') == -8

    # AND/LSHIFT/ASSIGN/NOT operations
    day07.operations={
        'a': ['AND', '1', 'b'],
        'b': ['LSHIFT', 'c', '1'],
        'c': ['ASSIGN', 'd', None],
        'd': ['NOT', '66000', None]
    }
    assert day07.resolve('a') == 0
    assert day07.resolve('b') == -132002

    