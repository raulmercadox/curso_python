# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:39:24 2019

@author: ezmerra
"""

# Write a program that asks the user to input 10 integers, and then prints the
# largest odd number that was entered. If no odd number was entered, it should
# print a message to that effect

i = 0
first = True
max_odd = 0
while i < 10:
    number = int(input('Specify number #' + str(i + 1) + ': '))
    if first == True:
        if number % 2 != 0:
            # It is an odd number
           max_odd = number
           first = False
    else:
        if number % 2 != 0:
            # It is an odd number
            if number > max_odd:
                max_odd = number
    i += 1
if max_odd == 0:
    print('No odd numbers were entered')
else:
    print('The maximum odd number that was entered is:', max_odd)