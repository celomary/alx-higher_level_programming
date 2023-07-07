#!/usr/bin/python3
"""Defines an say_my_name function."""


def say_my_name(first_name, last_name=""):
    """
    Generate a full name based on the given first name and last name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.

    Returns:
        str: The generated full name. If the last name is not provided or
             is an empty string, only the first name is returned.

    Raises:
        TypeError: If the first_name or last_name is not a string.

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if not last_name:
        return first_name
    return first_name + " " + last_name
