# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 13:29:18 2019

@author: ezmerra
"""
x = 3
def g(x):
    x = x + 1
    def h():
        x = x + 2
        print(x)
    
    print('in g(x): x =', x)
    h()
    return x


z = g(x)
print(z)