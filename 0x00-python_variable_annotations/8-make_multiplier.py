#!/usr/bin/python3

"""
This module demonstrates type annotations in
python with a type-annotated function make_multiplier
that takes a float multiplier as argument and returns a
function that multiplies a float by multiplier.


Function:
    make_multiplier(multiplier: float) -> Callable[[float], float]:
        return a function that multiplies a float by multiplier.

Imports:
    The type Callable is imported from the typing module and is used
    to annotate the return value of the make_multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:

    """
    Return a function that multiplies a float by a multiplier

    Args:
        multiplier (float): A value that will be multiplied by
        the value that will be passed to the return function as
        argument, which will be the return value of the return
        function.

    Return:
        func: A function that multiplies a float by a multiplier.

    Raises:
        TypeError if multiplier is not a float.

    Example:
        >>> fun = make_multiplier(2.0)
        >>> callable(fun)
        True
        >>> fun(4.0)
        8.0
        >>> fun = make_multiplier(2)
        Traceback (most recent call last):
            ...
        TypeError: multiplier must be a float
        >>> fun = make_multiplier("dog")
        Traceback (most recent call last):
            ...
        TypeError: multiplier must be a float

    """
    if not isinstance(multiplier, float):
        raise TypeError('multiplier must be a float')

    def multiplier_func(val: float) -> float:
        return val * multiplier

    return multiplier_func


# Run docstring tests if run as main module
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
