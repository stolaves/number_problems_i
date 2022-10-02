import pytest
import math
import random
import number_problems_1 as prog

@pytest.mark.parametrize(('n', 'res'), [(1, 1), 
                                        (2, 2),
                                        (6, 6), 
                                        (10, 19), 
                                        (11, 29), 
                                        (12, 39),
                                        (13, 49),
                                        (30, 3999),
                                        (43, 79999),
                                        (93, 39999999999),
                                        (130, 499999999999999), 
                                        (215, 899999999999999999999999),
                                        (560, 299999999999999999999999999999999999999999999999999999999999999), 
                                        (854, 89999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999),
                                        (934, 79999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)])

def test_smallest_n_sum(n, res):
    assert prog.smallest_n_sum(n) == res

@pytest.mark.parametrize(('n'), [(-1),(-5),(0.0000520001),("3dg25aa"),("6523nsnf")])
def test_smallest_n_sum_exceptions( n):
    with pytest.raises(ValueError):
        prog.smallest_n_sum(n)