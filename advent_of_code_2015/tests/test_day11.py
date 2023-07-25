from unittest.mock import mock_open, patch

import pytest
from solutions import day11


def test_create_input():
    with patch('builtins.open', mock_open(read_data='hijklmmn\n')):
        returns = day11.create_input()
        assert returns == 'hijklmmn'


@pytest.mark.parametrize(
    'string, valid', [
        ('hijklmmn', False),  
        ('abbceffg', False),  
        ('abbcegjk', False),  
        ('abcdffaa', True),  
        ('ghjaabcc', True),
        ('ghjaabaa', False),
    ]
)
def test_is_valid_password(string, valid):
    returns = day11.is_valid_password(string)
    assert returns == valid
