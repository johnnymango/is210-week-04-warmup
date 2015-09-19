#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """This function creates a formatted string using its two arguments and a
        separate variable.

        The first argument is repeated by the number of times passed in the
        second argument. The string is further formatted by adding the nudges
        variable; the nudges variable is also repeated the number of
        times passed in second argument.

    Args:
        wink (str):  The string variable that is added to the string via the
        format() function and repeated.
        numwink (int, optional): The number of times the wink and nudges
        variables are repeated in the string. Default: 2

    Returns:
        str: The string formatted with the wink, repeated the
        number of times set by the numwink.  The string is further formatted
        with the nudge variable repeated the number of times passed in numwink.

    Examples:

        >>>know_what_i_mean('Johnny')
        'Know what I mean? JohnnyJohnny, nudge nudge'

        >>>know_what_i_mean('Homer', 3)
        'Know what I mean? HomerHomerHomer, nudge nudge nudge'
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
