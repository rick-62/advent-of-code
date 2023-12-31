from unittest.mock import mock_open, patch

import numpy as np
import pytest
import pytest_timeout
from solutions import day18


@pytest.mark.parametrize(
    'example_input, expected_outcome', [(
        '''#.#\n..#\n...''',
        np.array([[1,0,1], [0,0,1], [0,0,0]])
    )]
)
def test_create_input(example_input, expected_outcome):
    with patch('builtins.open', mock_open(read_data=example_input)):
        array = day18.create_input()
        assert np.array_equal(array, expected_outcome)


@pytest.mark.parametrize(
    'arr, result', [(
        np.array([
            [0,1,0,1,0,1], 
            [0,0,0,1,1,0],
            [1,0,0,0,0,1],
            [0,0,1,0,0,0],
            [1,0,1,0,0,1],
            [1,1,1,1,0,0],
        ]),
        np.array([
            [0,0,1,1,0,0], 
            [0,0,1,1,0,1],
            [0,0,0,1,1,0],
            [0,0,0,0,0,0],
            [1,0,0,0,0,0],
            [1,0,1,1,0,0],
        ]),
    ),
    (
        np.array([
            [1,1,0,1,0,1], 
            [0,0,0,1,1,0],
            [1,0,0,0,0,1],
            [0,0,1,0,0,0],
            [1,0,1,0,0,1],
            [1,1,1,1,0,1],
        ]),
        np.array([
            [0,0,1,1,0,0], 
            [1,1,1,1,0,1],
            [0,0,0,1,1,0],
            [0,0,0,0,0,0],
            [1,0,0,0,1,0],
            [1,0,1,1,1,0],
        ]),
    ),
    ]
)
def test_animate_lights(arr, result):
    assert np.array_equal(day18.animate_lights(arr), result)
