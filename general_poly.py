# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 19:43:24 2019

@author: ezmerra
"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    
    def poly(base):
        total = 0
        indice = 1
        ancho = len(L)
        for elemento in L:
            total += elemento * (base ** (ancho - indice))
            indice += 1
        return total
    
    return poly
    
        