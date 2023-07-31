from unittest.mock import mock_open, patch

import pytest
import pytest_timeout
from solutions import day13


@pytest.mark.parametrize(
    'example_input', [
        (
            '''
            Alice would gain 54 happiness units by sitting next to Bob.
            Alice would lose 79 happiness units by sitting next to Carol.
            Alice would lose 2 happiness units by sitting next to David.
            Bob would gain 83 happiness units by sitting next to Alice.
            Bob would lose 7 happiness units by sitting next to Carol.
            Bob would lose 63 happiness units by sitting next to David.
            Carol would lose 62 happiness units by sitting next to Alice.
            Carol would gain 60 happiness units by sitting next to Bob.
            Carol would gain 55 happiness units by sitting next to David.
            David would gain 46 happiness units by sitting next to Alice.
            David would lose 7 happiness units by sitting next to Bob.
            David would gain 41 happiness units by sitting next to Carol.
            '''
        ),
    ]
)
def test_create_input(example_input):
    with patch('builtins.open', mock_open(read_data=example_input)):
        returns = day13.create_input()
        assert len(returns) == 14


@pytest.mark.parametrize(
    'lst, expected_weights, expected_names', [
        (
            ['Alice would gain 54 happiness units by sitting next to Bob.'], 
            {('Alice', 'Bob'): 54}, 
            set(['Alice', 'Bob'])
        ),
        (
            ['Bob would lose 63 happiness units by sitting next to David.' ], 
            {('Bob', 'David'): -63}, 
            set(['David', 'Bob'])
        ),
        (
            [
                'Bob would lose 63 happiness units by sitting next to David.', 
                'David would lose 7 happiness units by sitting next to Bob.'
            ], 
            {('Bob', 'David'): -70}, 
            set(['David', 'Bob'])
        ),
        (
            [
                'Bob would lose 7 happiness units by sitting next to Carol.', 
                'Carol would gain 60 happiness units by sitting next to Bob.'
            ], 
            {('Bob', 'Carol'): 53}, 
            set(['Carol', 'Bob'])
        ),
    ]
)
def test_parse_input(lst, expected_weights, expected_names):
    names, weights = day13.parse_input(lst)
    assert weights == expected_weights
    assert names == expected_names


@pytest.mark.parametrize(
    'example_input, expected_score,', [
        (
            '''
            Alice would gain 54 happiness units by sitting next to Bob.
            Alice would lose 79 happiness units by sitting next to Carol.
            Alice would lose 2 happiness units by sitting next to David.
            Bob would gain 83 happiness units by sitting next to Alice.
            Bob would lose 7 happiness units by sitting next to Carol.
            Bob would lose 63 happiness units by sitting next to David.
            Carol would lose 62 happiness units by sitting next to Alice.
            Carol would gain 60 happiness units by sitting next to Bob.
            Carol would gain 55 happiness units by sitting next to David.
            David would gain 46 happiness units by sitting next to Alice.
            David would lose 7 happiness units by sitting next to Bob.
            David would gain 41 happiness units by sitting next to Carol.
            ''', 330
        ),
    ]
)
def test_find_optimal_seating_arrangement(example_input, expected_score):
    with patch('builtins.open', mock_open(read_data=example_input)):
        names, weights = day13.parse_input(day13.create_input())
        score, _ = day13.find_optimal_seating_arrangement(names, weights)
        assert score == expected_score