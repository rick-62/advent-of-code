from unittest.mock import mock_open, patch

import pytest
from solutions import day08


def test_lookup():
    pass


# @pytest.mark.parametrize(
#     's, op, X, Y, Z', [
#         ('123 -> x', 'ASSIGN', '123', None, 'x'),  
#         ('456 -> y', 'ASSIGN', '456', None, 'y'),  
#         ('x AND y -> d', 'AND', 'x', 'y', 'd'),  
#         ('x OR y -> e', 'OR', 'x', 'y', 'e'),  
#         ('x LSHIFT 2 -> f', 'LSHIFT', 'x', '2', 'f'),  
#         ('y RSHIFT 2 -> g', 'RSHIFT', 'y', '2', 'g'),  
#         ('NOT x -> h', 'NOT', 'x', None, 'h'),  
#         ('NOT y -> i', 'NOT', 'y', None, 'i'),  
#         ('gk AND gq -> gs', 'AND', 'gk', 'gq', 'gs'),  
#         ('1 AND gd -> ge', 'AND', '1', 'gd', 'ge'),  
#         ('NOT y -> i', 'NOT', 'y', None, 'i'),  
#         ('NOT y -> i', 'NOT', 'y', None, 'i'),  
#         ('NOT y -> i', 'NOT', 'y', None, 'i'),  
#     ]
# )
# def test_create_input(s, op, X, Y, Z):
#     with patch('builtins.open', mock_open(read_data=s)):
#         returns = day08.create_input()
#         assert returns[Z] == [op, X, Y]

