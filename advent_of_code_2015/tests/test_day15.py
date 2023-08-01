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
    output = day15.parse_input(example_input)
    assert output == expected_output


