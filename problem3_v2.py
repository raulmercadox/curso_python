# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 18:45:00 2019

@author: ezmerra
"""
s = 'azcbobobegghakl'
#s = 'abcbcd'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
acum = ''
old_index = -1
for letter in s:
    index = alphabet.index(letter)
    acum += letter if index >= old_index else '|' + letter
    old_index = index

mayor = ''
actual = ''
for letter in acum:
    if letter != '|':
        actual += letter
    else:
        mayor = actual if len(actual) > len(mayor) else mayor
        actual = ''

mayor = actual if len(actual) > len(mayor) else mayor

print('Longest substring in alphabetical order is:', mayor)