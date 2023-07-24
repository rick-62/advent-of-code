from unittest.mock import mock_open, patch

import pytest
from solutions import day09


@pytest.mark.parametrize(
    'line, start, end, distance', [
        ('London to Dublin = 464', 'London', 'Dublin', 464),  
        ('London to Belfast = 518', 'London', 'Belfast', 518),  
        ('Dublin to Belfast = 141', 'Dublin', 'Belfast', 141),  
    ]
)
def test_create_network(line, start, end, distance):
    graph = day09.create_network([line])
    assert graph[start][end]['weight'] == distance