import pytest
from solutions import day05


class TestString:

    @pytest.mark.parametrize(
        's, ans', [
            ('aei', True), 
            ('xazegov', True),
            ('aeiouaeiouaeiou', True),
            ('tttttttttttttt', False),
            ('ttttttttaettt', False)
        ]
    )
    def test_contains_three_vowels(self, s, ans):
        string = day05.String(s)
        assert string.contains_three_vowels() == ans


    @pytest.mark.parametrize(
        's, ans', [
            ('abcdde', True), 
            ('xx', True),
            ('aabbccdd', True),
            ('tytytyt', False),
            ('lasdkjfh', False)
        ]
    )
    def test_has_repeated_letter(self, s, ans):
        string = day05.String(s)
        assert string.has_repeated_letter() == ans


    @pytest.mark.parametrize(
        's, ans', [
            ('ab', False), 
            ('cd', False),
            ('pq', False),
            ('xy', False),
            ('lasdkjfh', True)
        ]
    )
    def test_no_forbidden_substrings(self, s, ans):
        string = day05.String(s)
        assert string.no_forbidden_substrings() == ans

    @pytest.mark.parametrize(
        's, ans', [
            ('ugknbfddgicrmopn', True), 
            ('aaa', True),
            ('jchzalrnumimnmhp', False),
            ('haegwjzuvuyypxyu', False),
            ('dvszwmarrgswjxmb', False)
        ]
    )
    def test_naughty_or_nice(self, s, ans):
        string = day05.String(s)
        assert string.naughty_or_nice() == ans

    
    @pytest.mark.parametrize(
        's, ans', [
            ('xyxy', True), 
            ('aabcdefgaa', True),
            ('jchzalrnumimnmhp', False),
            ('jcchzalrnumimnmhp', False),
            ('jcchzalrnuccmimnmhp', True),
            ('aaa', False),
            ('aaaaa', True),
            ('aaaa', True),
        ]
    )
    def test_contains_repeating_pair(self, s, ans):
        string = day05.String(s)
        assert string.contains_repeating_pair() == ans


    @pytest.mark.parametrize(
        's, ans', [
            ('xyxy', True), 
            ('aabcdefgaa', False),
            ('jchzalrnumimnmhp', True),
            ('jcchzalrnumimnmhp', True),
            ('jcchzalrnuccmimnmhp', True),
            ('aaa', True),
            ('aaaaa', True),
            ('aaaa', True),
            ('abcdefeghi', True)
        ]
    )
    def test_contains_repeated_letter(self, s, ans):
        string = day05.String(s)
        assert string.contains_repeated_letter() == ans
        