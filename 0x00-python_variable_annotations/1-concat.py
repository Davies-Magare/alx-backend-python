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
        str1(string) : The first string to be concantenated to the 
                       second string
        str2(string) : The second string to be concantenated to the
                        first string

    Returns:
        str: The result of concantenating str1 and str2
    Example:
        >>> concat("Davies", " Magare")
        'Davies Magare'
        >>> concat('', '')
        ''
        >>> concat("egg", "shell") == "{}{}".format("egg", "shell")
        True
        >>> concat(4, "dog")
        Traceback (most recent call last):
            ...
        TypeError: unsupported operand type(s) for +: 'int' and 'str'
        >>> concat("dog", 4)
        Traceback (most recent call last):
            ...
        TypeError: can only concatenate str (not "int") to str

    """
    return str1 + str2
