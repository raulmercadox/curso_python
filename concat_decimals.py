# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:48:34 2019

@author: ezmerra
"""

# Let s be a string that contains a sequence of decimal numbers separated by
# commas, e.g., s = '1.23,2.4,3.123'. Write a program that prints the sum of
# the numbers in s.

s = '1.23,2.4,3.123'
number = ''
acum = 0
for l in s:
    if l != ',':
        number = number + l
    else:
        acum = acum + float(number)
        number = ''
acum = acum + float(number)
print(acum)