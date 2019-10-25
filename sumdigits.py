# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 12:48:20 2019

@author: ezmerra
"""

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    suma = 0
    hay_digitos = False
    for letter in s:
        if letter in '01234567890':
            hay_digitos = True
            suma += int(letter)
    if not hay_digitos:
        raise ValueError('There are no digits into the argument s')
    return suma

            