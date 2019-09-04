# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:03:23 2019

@author: ezmerra
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    menor = a if a < b else b
    while menor >= 1:
        if a % menor == 0 and b % menor == 0:
            break;
        menor -= 1
    return menor
