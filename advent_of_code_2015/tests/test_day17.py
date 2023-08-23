from unittest.mock import mock_open, patch

import numpy as np
import pytest
import pytest_timeout
from solutions import day17


@pytest.mark.parametrize(
    'example_input', [(
        '''
        1
        2
        3
        4
        5
        '''
    )]
)
def test_create_input(example_input):
    with patch('builtins.open', mock_open(read_data=example_input)):
        lines = day17.create_input()
        assert len(lines) > 0


# @pytest.mark.parametrize(
#     'example_input, expected_output', [
#         (
#             "Sue 1: goldfish: 9, cars: 0, samoyeds: 9", 
#             {'goldfish': 9, 'cars': 0, 'samoyeds': 9}
#         ),
#         (
#             "Sue 3: pomeranians: 2, akitas: 1, trees: 5", 
#             {'pomeranians': 2, 'akitas': 1, 'trees': 5}
#         ),
#         (
#             "Sue 1: goldfish: 10, cats: 9, cars: 8", 
#             {'goldfish': 10, 'cats': 9, 'cars': 8}
#         ),
#     ]
# )
# def test_create_input(example_input, expected_output):
#     assert day16.parse_input([example_input]) == [expected_output]