import math


def to_natural(n):
    pass


def is_square(n):
    if not is_natural(n):
        raise ValueError

    n = to_natural(n)

    root = n ** 0.5  # Raising to the power of half is same as square root

    if int(root) == root:
        return True
    else:
        return False


def digit_sum(n):
    pass


def hexagonal_number(n):
    pass


def factorial(n):
    pass


def smallest_digit_sum(n):
    pass
