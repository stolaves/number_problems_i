import pytest
import math
import random
import number_problems_1 as prog

@pytest.mark.parametrize(('n', 'res'), [(1, 1), 
                                        (2, 2),
                                        (12, 3),
                                        (15, 6),
                                        (17, 8),
                                        (60, 6),
                                        (112, 4),
                                        (653, 14), 
                                        (5134, 13),
                                        (8308, 19),
                                        (9167, 23),
                                        (7761, 21),
                                        (71894, 29),
                                        (27682558, 43), 
                                        (93954628213004808295, 88)])
def test_digit_sum( n, res):
    assert prog.digit_sum(n) == res

@pytest.mark.parametrize(('n'), [(-63),
                                 (-5),
                                 (0.00000001),
                                 ("32.a"),
                                 ("6f")])
def test_digit_sum_exceptions( n):
    with pytest.raises(ValueError):
        prog.digit_sum(n)