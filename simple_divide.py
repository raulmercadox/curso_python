# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:05:54 2019

@author: ezmerra
"""

def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0
    