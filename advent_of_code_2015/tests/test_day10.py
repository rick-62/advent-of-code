from unittest.mock import mock_open, patch

import pytest
from solutions import day10


def test_create_input():
    with patch('builtins.open', mock_open(read_data='111221\n')):
        returns = day10.create_input()
        assert returns == '111221'


@pytest.mark.parametrize(
    'digits, next_seq', [
        ('1', '11'),  
        ('11', '21'),  
        ('21', '1211'),  
        ('1211', '111221'),  
        ('111221', '312211'),  
    ]
)
def test_create_network(digits, next_seq):
    returns = day10.solve_next_sequence(digits)
    assert returns == next_seq
