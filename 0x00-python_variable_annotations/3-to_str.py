#!/usr/bin/env python3
"""This module demonstrates basic type annotations in Python
with a function that converts a floating-point number to a string
representation

Functions:
    to_str(n: float) -> str:
        Converts a floating-point number to its string representation
"""


def to_str(n: float) -> str:
    """
    Converts a floating-point number to its string representation
    Args:
        n(float): The floating-point number to be converted

    Returns:
        str: The string representation of the input floating point number
    Tests:
    >>> to_str(3.14)
    '3.14'
    >>> to_str(0.001)
    '0.001'
    >>> to_str(-42.0)
    '-42.0'

    """
    return str(n)
