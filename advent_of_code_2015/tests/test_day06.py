from collections import namedtuple
from unittest.mock import mock_open, patch

import pytest
from solutions import day06


class TestLights:

    def test_array_initialisation(self):
        lights = day06.Lights()
        assert lights.arr[0,0] == 0
        assert lights.arr[999,999] == 0
        assert lights.arr.shape == (1000,1000)

    def test_fn_on_off_toggle(self):
        lights = day06.Lights()

        # lights on
        lights.fn_on(5, 5, 10, 10)
        assert lights.arr[55,55] == 0
        assert lights.arr[5,5] == 1
        assert lights.arr[6,9] == 1

        # lights off
        lights.fn_off(0, 0, 7, 8)
        assert lights.arr[5,5] == 0
        assert lights.arr[6,7] == 0

        # toggle lights
        lights.fn_toggle(0, 0, 7, 8)
        assert lights.arr[5,5] == 1
        assert lights.arr[6,7] == 1
        assert lights.arr[0,0] == 1
        assert lights.arr[55,55] == 0

    def test_apply(self):
        lights = day06.Lights()
        Instruction = namedtuple("Instruction", ["instruction", "x1", "y1", "x2", "y2"])
        lights.apply(Instruction(instruction='turn on', x1=0, y1=0, x2=10, y2=10))
        assert lights.arr[0,9] == 1
        assert lights.arr[11,11] == 0

    def test_range(self):
        lights = day06.Lights()
        lights.fn_on(0, 0, 1000, 1000)
        assert lights.arr.sum() == 1_000_000


class TestAdvancedLights:

    def test_fn_on_off_toggle(self):
        lights = day06.AdvancedLights()

        # lights off
        lights.fn_off(0, 0, 10, 10)
        assert lights.arr[5,5] == 0

        # lights on
        lights.fn_on(0, 0, 10, 10)
        assert lights.arr[5,5] == 1

        # lights on (again)
        lights.fn_on(0, 0, 10, 10)
        assert lights.arr[5,5] == 2

        # toggle lights
        lights.fn_toggle(0, 0, 10, 10)
        assert lights.arr[5,5] == 4

        # lights off (again)
        lights.fn_off(0, 0, 10, 10)
        assert lights.arr[5,5] == 3
    
    def test_range(self):
        lights = day06.AdvancedLights()
        lights.fn_toggle(0, 0, 1000, 1000)
        assert lights.arr.sum() == 2_000_000


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
        assert returns[0].x2 == x2 + 1
        assert returns[0].y2 == y2 + 1



