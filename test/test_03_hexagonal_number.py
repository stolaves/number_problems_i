import pytest
import math
import random
import number_problems_1 as prog

@pytest.mark.parametrize(('n', 'res'), [(1, 7), 
                                        (2, 19), 
                                        (3, 37), 
                                        (4, 61), 
                                        (5, 91),
                                        (16, 817),
                                        (45, 6211), 
                                        (151, 68857), 
                                        (180, 97741), 
                                        (225, 152551), 
                                        (276, 229357),
                                        (580, 1010941),
                                        (1000, 3003001), 
                                        (6685, 134087731), 
                                        (9829,289857211)])
def test_hexagonal_number( n, res):
    assert prog.hexagonal_number(n) == res

@pytest.mark.parametrize(('n'), [(-63),(-5),(0.00000001),("32.a"),("6f")])
def test_hexagonal_number_exceptions( n):
    with pytest.raises(ValueError):
        prog.hexagonal_number(n)
