import pytest
from solutions import day02


class TestPerson:

    @pytest.mark.parametrize(
        'l, w, h, ans', [
        (2, 3, 4, 52), 
        (1, 1, 10, 42), 
        ]
    )
    def test_calculate_surface_area(self, l, w, h, ans):
        p = day02.Present(l=l, w=w, h=h)
        assert p.calculate_surface_area() == ans

    @pytest.mark.parametrize(
        'l, w, h, ans', [
        (2, 3, 4, 6), 
        (1, 1, 10, 1), 
        ]
    )
    def test_calculate_area_of_smallest_side(self, l, w, h, ans):
        p = day02.Present(l=l, w=w, h=h)
        assert p.calculate_area_of_smallest_side() == ans

    @pytest.mark.parametrize(
        'l, w, h, ans', [
        (2, 3, 4, 10), 
        (1, 1, 10, 4), 
        ]
    )
    def test_calculate_length_of_ribbon_for_present(self, l, w, h, ans):
        p = day02.Present(l=l, w=w, h=h)
        assert p.calculate_length_of_ribbon_for_present() == ans

    @pytest.mark.parametrize(
        'l, w, h, ans', [
        (2, 3, 4, 24), 
        (1, 1, 10, 10), 
        ]
    )
    def test_calculate_length_of_ribbon_for_bow(self, l, w, h, ans):
        p = day02.Present(l=l, w=w, h=h)
        assert p.calculate_length_of_ribbon_for_bow() == ans

    

    




