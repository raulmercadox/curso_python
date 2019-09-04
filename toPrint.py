# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:33:26 2019

@author: ezmerra
"""

# Finger exercise: Replace the comment in the following code with a while loop

numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
#concatenate X to toPrint numXs times
i = 0
while i < numXs:
    toPrint = toPrint + 'X'
    i += 1
print(toPrint)