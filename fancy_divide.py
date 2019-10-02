# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 20:48:12 2019

@author: ezmerra
"""

def fancy_divide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")

fancy_divide([0, 2, 4], 0)