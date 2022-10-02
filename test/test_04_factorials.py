import pytest
import math
import random
import number_problems_1 as prog

@pytest.mark.parametrize(('n', 'res'), [(1, 1),
                                        (2, 2), 
                                        (3, 6), 
                                        (4, 24), 
                                        (5, 120),
                                        (6, 720), 
                                        (7, 5040),  
                                        (8, 40320), 
                                        (9, 362880), 
                                        (10, 3628800), 
                                        (12, 479001600),  
                                        (13, 6227020800), 
                                        (18, 6402373705728000), 
                                        (22, 1124000727777607680000),
                                        (50, 30414093201713378043612608166064768844377641568960512000000000000)])
def test_factorials( n, res):
    assert prog.factorial(n) == res

@pytest.mark.parametrize(('n'), [(-5),(-1),(3523.124),("13220.7"),("a105g2")])
def test_factorials_exceptions( n):
    with pytest.raises(ValueError):
        prog.factorial(n)