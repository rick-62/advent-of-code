
from solutions import day01

def test_find_final_floor():
    assert day01.find_final_floor('(())') == 0
    assert day01.find_final_floor('(()(()(') == 3
    assert day01.find_final_floor('))(') == -1

def test_first_enters_basement():
    assert day01.first_enters_basement(')(())())') == 1
    assert day01.first_enters_basement('()())((())') == 5