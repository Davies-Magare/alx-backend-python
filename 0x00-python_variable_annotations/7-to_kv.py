#!/usr/bin/env python3

"""
This module demonstrates basic python variable annotations with a
type-annotated function to_kv that takes a string k and an int OR
float v as arguments and returns a tuple. The first element of the
tuple is the string k. The second element is the square of the int
/float v and should be annotated as a float.

Functions:
    to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
        Takes a string and an int/float and returns a tuple with
        the string as the first element and the square of the integer
        or float as the second element.

Imports: The types Union and Tuple are imported from the type module.
    Union is used to annotate v, the second parameter of the function
    to_kv and Tuple is used to annotate the return type of the function
    to_kv.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:

    """
    Take a string and integer/float as arguments and return
    a tuple with the string as the first element and the integer
    or float as the second element.

    Args:
        k (str): The first element of the result tuple.
        v (int | float) : The second element of the result tuple.

    Returns:
        A tuple with k as the first element and the square of v as the second
            element.

    Raises:
        TypeError: If k is not a string and v is not an integer or float.

    Example:
        >>> to_kv("dog", 2)
        ('dog', 4.0)
        >>> to_kv("dog", 2.0)
        ('dog', 4.0)
        >>> to_kv("dog", "dog")
        Traceback (most recent call last):
            ...
        TypeError: v must be an integer or a float
        >>> to_kv(4, 4.5)
        Traceback (most recent call last):
            ...
        TypeError: k must be a string

    """
    if isinstance(k, str) and (isinstance(v, int) or isinstance(v, float)):
        return (k, v * v)
    if not isinstance(k, str):
        raise TypeError('k must be a string')
    raise TypeError('v must be an integer or a float')


# Run docstring if run as main module

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
