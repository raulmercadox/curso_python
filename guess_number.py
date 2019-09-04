# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 19:21:21 2019

@author: ezmerra
"""

low = 0
high = 100

print("Please think of a number between 0 and 100!")

while True:
    guess = int((low + high) / 2)
    answer = ''
    first = True
    while answer != 'h' and answer != 'l' and answer != 'c':
        if not first:
            print("Sorry, I did not understand your input.")
        print("Is your secret number " + str(guess) + "?")
        print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.", end = ' ')
        answer = input()
        first = False
    if answer == 'h':
        high = guess
    if answer == 'l':
        low = guess
    if answer == 'c':
        print("Game over. Your secret number was: " + str(guess))
        break