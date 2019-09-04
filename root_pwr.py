# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:29:25 2019

@author: ezmerra
"""

# Write a program that asks the user to enter an integer and prints two 
# integers, root and pwr, such that 1 < pwr < 6 and root**pwr is equal to the
# integer entered by the user. If no such pair of integers exists, it should
# print a message to that effect

number = int(input('Enter an integer: '))
pwr = 2
found = False
while pwr < 6:
    root = 1
    while root**pwr < number:
        root += 1
    if root**pwr == number:
        print(str(root) + '**' + str(pwr) + ' = ' + str(number))
        found = True
        break
    pwr += 1
if found == False:
    print('no root and pwr found for', number)