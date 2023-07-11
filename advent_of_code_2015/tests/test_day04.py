import pytest
from solutions import day04


@pytest.mark.parametrize(
    'string, ans', [
        ('abcdef609043', '000001dbbfa'), 
        ('pqrstuv1048970', '000006136ef'),
    ]
)
def test_get_md5_hash(string, ans):
    assert day04.get_md5_hash(string).startswith(ans)


@pytest.mark.parametrize(
    'string, ans', [
        ('abcdef', 609043), 
        ('pqrstuv', 1048970),
    ]
)
def test_find_decimal_suffix_of_string(string, ans):
    assert day04.find_decimal_suffix_of_string(string) == ans




