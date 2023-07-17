from collections import namedtuple
from unittest.mock import mock_open, patch

import pytest
from solutions import day07


class TestOperation:

    def test_init(self):
        op = day07.Operation()
        assert op._lookup['AND'](1,1) == 1
        assert op._lookup['OR'](0,1) == 1
        assert op._lookup['LSHIFT'](1,1) == 2
        assert op._lookup['NOT'](1) == -2
        assert op._lookup['ASSIGN'](10) == 10

    # def test__resolve(self):
    #     op = day07.Operation()
    #     op.a = 3
    #     assert op._resolve(2) == 2
    #     assert op._resolve('2') == 2
    #     assert op._resolve('a') == 3

    def test_apply(self):
        op = day07.Operation()
        Operation = namedtuple("Operation", ["operator", "X", "Y", "Z"])

        op.apply(Operation(operator='ASSIGN', X='123', Y=None, Z='x'))
        assert op.x == 123

        op.apply(Operation(operator='NOT', X='x', Y=None, Z='h'))
        assert op.x == 123
        assert op.h == 65412

        op.apply(Operation(operator='AND', X='x', Y='456', Z='d'))
        assert op.x == 123
        assert op.d == 72


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
        assert returns[0].X == X
        assert returns[0].Y == Y
        assert returns[0].Z == Z
        assert returns[0].operator == op

    



