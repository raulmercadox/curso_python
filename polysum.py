# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 11:36:36 2019

@author: ezmerra
"""
import math

def polysum(n, s):
    area = (0.25 * n * s**2) / math.tan(math.pi / n)
    perimeter = n * s
    return round( area + perimeter**2, 4)