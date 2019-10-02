# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 17:15:14 2019

@author: ezmerra
"""

def count7(N):
    '''
    N: a non-negative integer
    '''
    if N < 10:
        if N == 7:
            return 1
        else:
            return 0
    else:
        ultimo_digito = N % 10
        if ultimo_digito == 7:
            return 1 + count7(N // 10)
        else:
            return count7(N // 10)