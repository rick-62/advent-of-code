from unittest.mock import mock_open, patch

import numpy as np
import pytest
import pytest_timeout
from solutions import day15


@pytest.mark.parametrize(
    'example_input', [(
        '''
        Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
        Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
        '''
    )]
)
def test_create_input(example_input):
    with patch('builtins.open', mock_open(read_data=example_input)):
        lines = day15.create_input()
        assert len(lines) > 0


@pytest.mark.parametrize(
    'example_input, expected_output', [(
            [
                'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8', 
                'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'
            ],
            np.array([
                [-1, 2],
                [-2, 3],
                [6, -2],
                [3, -1],
                [8, 3],
            ])
            ,
        )]
)
def test_parse_input_properties(example_input, expected_output):
    properties = day15.parse_input(example_input)
    assert np.array_equal(properties, expected_output)


def test_yield_teaspoon_combinations_for_four_ingredients():
    combination = day15.yield_teaspoon_combinations_for_four_ingredients()
    assert sum(next(combination)) == 100
    assert np.array_equal(next(combination), np.array([0,0,1,99]))


@pytest.fixture()
def properties1():
    return (
        np.array([
            [-1, 2],
            [-2, 3],
            [6, -2],
            [3, -1],
        ])
    )


@pytest.mark.parametrize(
    'example_teaspoons, expected_output', [
        (np.array([44,56]), 62842880),
        ]
)
def test_calculate_score(example_teaspoons, expected_output, properties1):
    score = day15.calculate_score(example_teaspoons, properties1)
    assert np.array_equal(score, expected_output)