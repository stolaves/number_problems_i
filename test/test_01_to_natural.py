import pytest
import math
import random
import number_problems_1 as prog


@pytest.mark.parametrize(('n', 'res'), [(1, 1), 
                                        (3, 3), 
                                        (n := random.randint(0,100), n),
                                        (n := random.randint(0,100), n),
                                        (random.randint(-100,-1), False),
                                        (random.randint(-100,-1), False),
                                        ("Hello",False),
                                        ("Fweri325",False),
                                        ("125dfwe",False),
                                        ("1", 1),("13", 13),
                                        (str(n:= random.randint(0,10000)),n),
                                        (str(n:= random.randint(0,10000)),n),
                                        (str(n:= random.randint(0,10000)),n),
                                        (str(float(n:= random.randint(0,10000))),n),
                                        (str(float(n:= random.randint(0,10000))),n),
                                        ("1.0",1),
                                        ("6.00000000000000000",1),
                                        (random.random(),False),
                                        (random.random(),False),
                                        (random.random(),False)])
def test_to_natural(n, res):
    assert prog.to_natural(n) == res