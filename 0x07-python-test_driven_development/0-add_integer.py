#!/usr/bin/python3
"""
This module provides an add_integer function that adds two numbers.
"""


def add_integer(a, b=98):
    """
    This function adds two integers or floats.
    If either of a or b is a float, it is cast to an integer.
    If either of a or b is not an integer or float, a TypeError is raised.

    Args:
        a (int or float): The first number, must be an integer or float.
        b (int or float, optional): The second number, must be an integer or float, default is 98.

    Returns:
        int: The sum of a and b, as an integer.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
