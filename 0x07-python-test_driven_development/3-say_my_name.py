#!/usr/bin/python3
"""
This is a module for printing a person's first and last name.
"""

def say_my_name(first_name, last_name=""):
    """
    Prints a name with the format "My name is <first_name> <last_name>".

    Args:
        first_name (str): The first name to be printed.
        last_name (str): The last name to be printed. Optional; defaults to empty string.

    Raises:
        TypeError: If either first_name or last_name is not a string.
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")
    print(f"My name is {first_name} {last_name}")
