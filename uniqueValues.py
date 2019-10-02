# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 18:41:15 2019

@author: ezmerra
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    lista_keys = []
    valores = []
    for valor in aDict.values():
        valores.append(valor)
        
    for clave in aDict:
        if type(aDict[clave]) == int:
            if valores.count(aDict[clave]) == 1:
                lista_keys.append(clave)
                
    return lista_keys
        