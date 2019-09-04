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
    index = 0
    for l in alphabet:
        if letter == l:
            if index >= old_index:
                acum += letter
            else:
                acum += '|' + letter
            old_index = index
            break
        index += 1

mayor = ''
actual = ''
for letter in acum:
    if letter != '|':
        actual += letter
    else:
        if len(actual) > len(mayor):
            mayor = actual
        actual = ''

if len(actual) > len(mayor):
    mayor = actual

print('Longest substring in alphabetical order is:', mayor)