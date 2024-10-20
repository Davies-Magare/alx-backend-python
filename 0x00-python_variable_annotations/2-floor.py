#!/usr/bin/env python3

"""This module demonstrates basic type annotations in Python
with a function that converts a float to its floor integer

Imports:
    math: Used for the floor function to compute the largest
        integer less or equal to the given float.

Functions:
    floor(n: float) -> int:
        Converts a float to its floor.
"""


import math


def floor(n: float) -> int:
    """
    Converts a float to its floor integer

    Args:
        n (float): The only parameter: A floating-point number
            to convert to its floor integer.

    Returns:
        int: The integer floor of n.

    Example:
        >>> floor(3.5)
        3
        >>> floor(-4)
        Traceback (most recent call last):
                ...
        TypeError: n must be a floating-point number

    Raises:
        TypeError: If n is not a floating-point number.

    """
    if not isinstance(n, float):
        raise TypeError('n must be a floating-point number')

    return math.floor(n)


# If running this module directly, execute doctests.
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
