from unittest.mock import mock_open, patch

import numpy as np
import pytest
import pytest_timeout
from solutions import day19


@pytest.mark.parametrize(
    'example_input, expected_dict, expected_molecule', [
        ("H => HO\nH => OH\nO => HH\n\nHOH\n", {'H': ["HO", "OH"], 'O': ["HH"]}, "HOH"),
        ("Ti => HO\nTi => OH\nO => HH\n\nHOH\n", {'Ti': ["HO", "OH"], 'O': ["HH"]}, "HOH")
    ]
)
def test_create_input(example_input, expected_dict, expected_molecule):
    with patch('builtins.open', mock_open(read_data=example_input)):
        actual_dict, actual_molecule = day19.create_input()
        assert actual_dict == expected_dict
        assert actual_molecule == expected_molecule


@pytest.mark.parametrize(
    'replacements_dict, molecule, expected_molecules', [
        ({'H': ["HO", "OH"], 'O': ["HH"]}, "HOH", {"HOOH", "HOHO", "OHOH", "HHHH"}),
        ({'Ho': ["HO"]}, "CHoP", {"CHOP"})
    ]
)
def test_generate_molecules(replacements_dict, molecule, expected_molecules):
    generated_molecules = day19.generate_molecules(replacements_dict, molecule)
    assert generated_molecules == expected_molecules  


@pytest.mark.parametrize(
    'start, end, replacements, expected_output', [
        (
            "Hello ", " World", ["Cruel", "Happy", "Funny"], 
            {"Hello Cruel World", "Hello Happy World", "Hello Funny World"}
        ),
        (
            "A", "C", ["B", "D", "E"], 
            {"ABC", "ADC", "AEC"}
        ),
    ]
)
def test_insert_replacements(start, end, replacements, expected_output):
    generated_molecules = day19.insert_replacements(start, end, replacements)
    assert set(generated_molecules) == expected_output 