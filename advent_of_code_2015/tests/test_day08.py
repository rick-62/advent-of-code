from unittest.mock import mock_open, patch

import pytest
from solutions import day08


@pytest.mark.parametrize(
    'string, length', [
        (r'""', 2),  
        (r'"abc"', 5),  
        (r'"aaa\"aaa"', 10),  
        (r'"\x27"', 6),  
    ]
)
def test_create_input(string, length):
    with patch('builtins.open', mock_open(read_data=string)):
        returns = day08.create_input()
        assert returns[0] == string
        assert len(returns[0]) == length


@pytest.mark.parametrize(
    'str_in, str_out', [
        (r'""', ''),  
        (r'"abc"', 'abc'),  
        (r'"aaa\"aaa"', 'aaa#aaa'),  
        (r'"\x27"', '#'),  
    ]
)
def test_evaluate_string(str_in, str_out):
    assert day08.evaluate_string(str_in) == str_out


@pytest.mark.parametrize(
    'str_in, str_out, length', [
        (r'""', '"#"#""', 6),  
        (r'"abc"', '"#"abc#""', 9),  
        (r'"aaa\"aaa"', '"#"aaa###"aaa#""', 16),  
        (r'"\x27"', '"#"######""', 11),  
    ]
)
def test_encode_strings(str_in, str_out, length):
    assert day08.encode_string(str_in) == str_out
    assert len(day08.encode_string(str_in)) == length