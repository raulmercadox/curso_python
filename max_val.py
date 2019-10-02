# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 19:04:16 2019

@author: ezmerra
"""

def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t 
        For example,
        max_val((5, (1,2), [[1],[2]])) returns 5 .
        max_val((5, (1,2), [[1],[9]])) returns 9 .
    """ 
    lista = obtener_lista(t)
    return max(lista)

def obtener_lista(t):
    lista = []
    for elemento in t:
        if type(elemento) == int:
            lista.append(elemento)
        else:
            sub_lista = obtener_lista(elemento)
            lista.extend(sub_lista)
    return lista