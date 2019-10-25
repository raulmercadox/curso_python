# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 12:57:23 2019

@author: ezmerra
"""

def longestRun(L):
    ancho = len(L)
    if ancho == 0 or ancho == 1:
        return ancho
    
    anterior = None
    contador = 0
    maximo_ancho = 0
    for i in L:
        if anterior == None:
            anterior = i
            contador += 1
        else:
            if i >= anterior:
                contador += 1
            else:
                if contador > maximo_ancho:
                    maximo_ancho = contador
                contador = 1
            anterior = i
    if contador > maximo_ancho:
        maximo_ancho = contador
    return maximo_ancho

"""
assert longestRun([])==0
assert longestRun([2])==1
assert longestRun([1,2])==2
assert longestRun([2,1])==1
assert longestRun([1,2,1,2])==2
assert longestRun([1,2,3,1,2])==3
assert longestRun([1,2,2,3,1,2])==4
assert longestRun([1,2,1,2,2,3])==4
assert longestRun([1,2,1,2,2,3,6,7])==6
assert longestRun([1,2,1,2,2,3,1,7,8,8,9])==5
assert longestRun([1,2,1,2,2,3,5,1,7,8,8,9])==5
"""


            
        
    
    