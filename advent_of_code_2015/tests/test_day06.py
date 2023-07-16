from unittest.mock import patch, mock_open

import pytest
from solutions import day06


class TestLights:

    def test_array_initialisation(self):
        lights = day06.Lights()
        assert lights.arr[0,0] == 0
        assert lights.arr[999,999] == 0
        assert lights.arr.shape == (1000,1000)


@pytest.mark.parametrize(
    's, i, x1, y1, x2, y2', [
        ('turn on 0,0 through 999,999', 'turn on', 0, 0, 999, 999), 
        ('toggle 0,0 through 999,0', 'toggle', 0, 0, 999, 0), 
        ('turn off 499,499 through 500,500', 'turn off', 499, 499, 500, 500), 
    ]
)
def test_create_input(s, i, x1, y1, x2, y2):
    with patch('builtins.open', mock_open(read_data=s)):
        returns = day06.create_input()
        assert returns[0].instruction == i
        assert returns[0].x1 == x1
        assert returns[0].y1 == y1
        assert returns[0].x2 == x2
        assert returns[0].y2 == y2



