#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module checks if there are enough litterboxes and food for kittens."""


def too_many_kittens(kittens, litterboxes, catfood):
    """Checks if there is enough litterboxes and food for each kitten.

    Args:
        kittens (int): The number of kittens.
        litterboxes (int):  The number of available litterboxes.
        catfood  (bool): Represents whether or not any catfood exists.  True
        if there is enough food; False if there is not enough food.

    Returns:
        Boolean. True if the there are not enough litterboxes or food for
        the kittens.  False if there are enough litterboxes and food for the
        kittens.

    Examples:

        >>>too_many_kittens(12, 5, True)
        True

        >>>too_many_kittens(12, 20, True)
        False

        >>>too_many_kittens(12, 20, False)
        True

    """
    return not (litterboxes >= kittens and catfood)