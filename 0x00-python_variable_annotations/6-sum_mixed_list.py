#!/usr/bin/env python3

"""
This module demonstrates type annotations with an
annotated function sum_mixed_list which takes a list
mxd_lst of integers and floats and returns their sum
as a float


Imports: The types List and Union are imported from the
    typing module to annotate the mxd_lst function parameter.

Function: sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float
    Calculates the sum of the values of a list of integers and floats

"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:

    """
    Calculates the sum of a list of integers and floats.

    Args:
        mxd_lst: The only parameter which is a list of integers
            and floats.

    Returns:
        float: The sum of the values of mxd_lst.


    Raises: TypeError if mxd_lst is not a list.


    Example:
        >>> sum_mixed_list([4, 4.5])
        8.5
        >>> sum_mixed_list([4.0, 4.5])
        8.5
        >>> sum_mixed_list([])
        0
        >>> sum_mixed_list("dog")
        Traceback (most recent call last):
            ...
        TypeError: mxd_lst must be a list
    """

    if not isinstance(mxd_lst, list):
        raise TypeError("mxd_lst must be a list")
    return sum(mxd_lst)


# If run as main modue run doctests
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
