# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:10:39 2019

@author: ezmerra
"""

varA = -3
varB = "goodbye"

if type(varA) == str or type(varB) == str:
    print("string involved")
elif varA > varB:
    print("bigger")
elif varA < varB:
    print("smaller")
else:
    print("equal")