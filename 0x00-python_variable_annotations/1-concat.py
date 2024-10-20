#!/usr/bin/env python3
"""This module demonstrates basic type annotations in Python
with a function that concantenates two strings

Functions:
    concat(str1: str, str2: str) -> str:
        Concantenates two strings
"""


def concat(str1: str, str2: str) -> str:
    """
    Concantenates two strings
    Args:
        str1(str) : The first string to be concatenated to the
                       second string
        str2(str) : The second string to be concatenated to the
                        first string

    Returns:
        str: The result of concatenating str1 and str2
    Example:
        >>> concat("Davies", " Magare")
        'Davies Magare'
        >>> concat('', '')
        ''

    Raises:
        TypeError: if either str1 or str2 is not a string

    """

    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both arguments must be strings.")

    return str1 + str2


# if running this module directly, execute doctests
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
