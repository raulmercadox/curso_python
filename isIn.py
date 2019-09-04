# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:52:40 2019

@author: ezmerra
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    middle = len(aStr) // 2
    
    if char == aStr[middle]:
        return True
    elif middle == 0:
        return False
    else:
        if char > aStr[middle]:
            return isIn(char, aStr[middle:])
        else:
            return isIn(char, aStr[:middle])
