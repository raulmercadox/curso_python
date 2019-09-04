# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 11:43:06 2019

@author: ezmerra
"""

def iterPower(base, exp):
    '''
    base: int or float
    exp: int > 0
    
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        i = 1
        prod = 1
        while i <= exp:
            prod = prod * base
            i = i + 1
        return prod