#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module sets default value in function definition."""


def defaults(my_required, my_optional=True):
    """Compares truthiness of two arguments.

    Args:
        my_required (mixed): The first argument in the comparison.
        my_optional (mixed, optional): The second argument in the comparison.
        The default is True.

    Returns:
        A boolean.  True if the first argument is the second argument.  False
        if the first argument is not the second argument.

    Examples:
        >>>defaults(True)
        True

        >>>defaults(True, False)
        False

        >>>defaults('cat', 'dog')
        False

        >>>>defaults(5, 5)
        True

    """
    return my_optional is my_required