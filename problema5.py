# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 19:54:49 2019

@author: ezmerra
"""

x = 12
def g(x):
    x = x + 1
    def h(y):
        return x + y
    return h(6)

print(g(x))