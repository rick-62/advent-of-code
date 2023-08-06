from unittest.mock import mock_open, patch

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
    'example_input, expected_output', [
        (
            [
                'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8', 
                'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'
            ],
            {
                'Butterscotch': {
                    'capacity': -1, 
                    'durability': -2, 
                    'flavor': 6, 
                    'texture': 3, 
                    'calories': 8
                },
                'Cinnamon': {
                    'capacity': 2, 
                    'durability': 3, 
                    'flavor': -2, 
                    'texture': -1, 
                    'calories': 3
                },
            },
    
        )
    ]
)
def test_parse_input(example_input, expected_output):
    output, _ = day15.parse_input(example_input)
    assert output == expected_output


@pytest.mark.parametrize(
    'example_input, expected_output', [
        (
            [
                'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8', 
                'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'
            ],
            {
                'capacity': {'Butterscotch': -1, 'Cinnamon': 2 },
                'durability': {'Butterscotch': -2, 'Cinnamon': 3 },
                'flavor': {'Butterscotch': 6, 'Cinnamon': -2 },
                'texture': {'Butterscotch': 3, 'Cinnamon': -1 }, 
                'calories': {'Butterscotch': 8, 'Cinnamon': 3 },
            },
    
        )
    ]
)
def test_parse_input_properties(example_input, expected_output):
    _, properties = day15.parse_input(example_input)
    assert properties == expected_output


