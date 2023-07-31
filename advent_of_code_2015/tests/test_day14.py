from unittest.mock import mock_open, patch

import pytest
import pytest_timeout
from solutions import day14


@pytest.mark.parametrize(
    'example_input', [
        ('Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.'),
        ('Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'),
    ]
)
def test_create_input(example_input):
    with patch('builtins.open', mock_open(read_data=example_input)):
        lines = day14.create_input()
        assert len(lines) == 1


@pytest.mark.parametrize(
    'lst, expected_name, expected_v, expected_t1, expected_t2', [
        (
            ['Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.'], 
            'Comet', 14, 10, 127
        ),
        (
            ['Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'], 
            'Dancer', 16, 11, 162
        ),
    ]
)
def test_parse_input(lst, expected_name, expected_v, expected_t1, expected_t2):
    reindeer = day14.parse_input(lst)
    obj = reindeer[expected_name]
    assert obj['v'] == expected_v
    assert obj['t1'] == expected_t1
    assert obj['t2'] == expected_t2


@pytest.mark.parametrize(
    't, v, t1, t2, expected_d', [
        (1000, 14, 10, 127, 1120),
        (1000, 16, 11, 162, 1056),
    ]
)
def test_distance_travelled(t, v, t1, t2, expected_d):
    assert day14.distance_travelled(t, v=v, t1=t1, t2=t2) == expected_d
