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
    'string, expected', [
        ([1,2,3], []),  
        ([1,{"c":"red","b":2},3], [{"c":"red","b":2}]),  
        ({"d":"red","e":[1,2,3,4],"f":5}, [{"d":"red","e":[1,2,3,4],"f":5}]),  
        ([1,"red",5], []),
        ({"a": 45,"c":{"b":"red"}}, [{"b":"red"}]),
        ({"a":45,"d":{"b": {"b":42},"c":{"f":"red"}}}, [{"f":"red"}]),
        ({"a":45,"d":{"b":{"c":42},"b":"red","c":{"d":{"e":1}}}}, [{"b":{"c":42},"b":"red","c":{"d":{"e":1}}}]),
    ]
)
def test_find_red_objects(string, expected):
    results = day12.find_red(string)
    assert results == expected
