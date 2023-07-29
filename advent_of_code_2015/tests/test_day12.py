from unittest.mock import mock_open, patch

import pytest
import pytest_timeout
from solutions import day12


def test_create_input():
    with patch('builtins.open', mock_open(read_data='{"e":[[{"e":86,"')):
        returns = day12.create_input()
        assert returns == '{"e":[[{"e":86,"'


@pytest.mark.parametrize(
    'string, output', [
        ('[1,2,3]', 6),  
        ('{"a":2,"b":4}', 6),  
        ('[[[3]]]', 3),  
        ('{"a":{"b":4},"c":-1}', 3),  
        ('{"a":[-1,1]}', 0),  
        ('[-1,{"a":1}]', 0),  
        ('{}', 0),  
        ('[]', 0),  

    ]
)
def test_sum_digits(string, output):
    returns = day12.sum_digits(string)
    assert returns == output


@pytest.mark.parametrize(
    'string, output', [
        ('[1,2,3]', 0),  
        ('[1,{"c":"red","b":2},3]', 2),  
        ('{"d":"red","e":[1,2,3,4],"f":5}', 15),  
        ('[1,"red",5]', 0),
        ('{"a": 45, {"b":"red"}}', 0),
        ('{"a": 45, {"b":"red", {"b": 42}}}', 42),
        ('{"a":45,{"b": {"b":42},{"f":"red"}}}}}', 0),
        ('{"a":45,{"b":{"c":42},"b":"red","c":{"d":{"e":1}}}}', 43),
    ]
)
def test_sum_digits(string, output):
    returns = day12.sum_digits_where_red(string)
    assert returns == output
