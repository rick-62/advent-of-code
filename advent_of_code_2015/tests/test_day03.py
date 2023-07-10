import pytest
from solutions import day03


@pytest.mark.parametrize(
    'movements, ans', [
    ('>', 2), 
    ('^>v<', 4),
    ('^v^v^v^v^v', 2), 
    ]
)
def test_count_visited_houses(movements, ans):
    log = day03.log_visited_houses(movements)
    assert day03.count_visited_houses(log) == ans

    
@pytest.mark.parametrize(
    'movements, ans', [
    ('^v', 3), 
    ('^>v<', 3),
    ('^v^v^v^v^v', 11), 
    ]
)
def test_count_visited_houses(movements, ans):
    movements1, movements2 = day03.unzip_movements_into_two(movements)
    log1 = day03.log_visited_houses(movements1)
    log2 = day03.log_visited_houses(movements2)
    assert day03.count_visited_houses(log1, log2) == ans
    




