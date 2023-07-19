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
        ('gk AND gq -> gs', 'AND', 'gk', 'gq', 'gs'),  
        ('1 AND gd -> ge', 'AND', '1', 'gd', 'ge'),  
        ('NOT y -> i', 'NOT', 'y', None, 'i'),  
        ('NOT y -> i', 'NOT', 'y', None, 'i'),  
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
    operations={
        'a': ['AND', 1, 2]
    }
    assert day07.resolve('a', operations) == 0

    # recurse
    operations={
        'b': ['AND', '1', 'c'],
        'c': ['LSHIFT', '1', '1'],
    }
    assert day07.resolve('b', operations) == 0

    # NOT operation
    operations={
        'd': ['NOT', '7', None],
    }
    assert day07.resolve('d', operations) == -8

    # AND/LSHIFT/ASSIGN/NOT operations
    operations={
        'e': ['AND', '1', 'f'],
        'f': ['LSHIFT', 'g', '1'],
        'g': ['ASSIGN', 'h', None],
        'h': ['NOT', '66000', None]
    }
    assert day07.resolve('e', operations) == 0
    assert day07.resolve('f', operations) == -132002


    