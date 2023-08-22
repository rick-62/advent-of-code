from unittest.mock import mock_open, patch

import numpy as np
import pytest
import pytest_timeout
from solutions import day16


@pytest.mark.parametrize(
    'example_input', [(
        '''
        Sue 1: goldfish: 9, cars: 0, samoyeds: 9
        Sue 2: perfumes: 5, trees: 8, goldfish: 8
        Sue 3: pomeranians: 2, akitas: 1, trees: 5
        Sue 4: goldfish: 10, akitas: 2, perfumes: 9
        Sue 5: cars: 5, perfumes: 6, akitas: 9
        Sue 6: goldfish: 10, cats: 9, cars: 8
        '''
    )]
)
def test_create_input(example_input):
    with patch('builtins.open', mock_open(read_data=example_input)):
        lines = day16.create_input()
        assert len(lines) > 0


@pytest.mark.parametrize(
    'example_input, expected_output', [
        (
            "Sue 1: goldfish: 9, cars: 0, samoyeds: 9", 
            {'goldfish': 9, 'cars': 0, 'samoyeds': 9}
        ),
        (
            "Sue 3: pomeranians: 2, akitas: 1, trees: 5", 
            {'pomeranians': 2, 'akitas': 1, 'trees': 5}
        ),
        (
            "Sue 1: goldfish: 10, cats: 9, cars: 8", 
            {'goldfish': 10, 'cats': 9, 'cars': 8}
        ),
    ]
)
def test_create_input(example_input, expected_output):
    assert day16.parse_input([example_input]) == [expected_output]