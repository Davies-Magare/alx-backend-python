#!/usr/bin/env python3

from typing import List

"""
This module demonstrates annotation in python with a type
annotated function sum_list which takes a list input_list
of floating-point values as argument and returns their sum as a floating-point
value.

Functions:
    sum_list(input_list: List[float]) -> float
        Calculates the sum of a list of floating-point values.

imports:
    List: Used to annotate the input_list parameter.
"""


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of floating-point values.

    Args:
        input_list (list): The only parameter which is a list of floating-
            point values.
    Returns:
        float: The sum of the floating-point values of the list.

    Raises:
        TypeError: If input_list is not a list.

    Example:
        >>> sum_list([4.5, 2.0])
        6.5
        >>> sum_list("four")
        Traceback (most recent call last):
            ...
        TypeError: input_list must be a list

    """
    if not isinstance(input_list, list):
        raise TypeError('input_list must be a list')
    return sum(input_list)


# If running this module directly, execute doctests

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
