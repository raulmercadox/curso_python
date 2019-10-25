# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 13:46:21 2019

@author: ezmerra
"""

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    r1 = {}
    r2 = {}
    for k1 in d1:
        if k1 in d2:
            r1[k1] = f(d1[k1], d2[k1])
        else:
            r2[k1] = d1[k1]
    
    for k2 in d2:
        if not k2 in d1:
            r2[k2] = d2[k2]
    
    return (r1, r2)

def f(a, b):
    return a > b

d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}

result = dict_interdiff(d1, d2)
print(result)