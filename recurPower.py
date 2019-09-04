# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 11:59:40 2019

@author: ezmerra
"""

def recurPower(base, exp):
    '''
    base: int or float
    exp: int > 0
    
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)