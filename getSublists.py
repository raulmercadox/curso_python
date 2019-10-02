# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 17:26:52 2019

@author: ezmerra
"""

def getSublists(L, n):
    resultado = []
    indice_inicial = 0
    ancho_L = len(L)
    while indice_inicial + n <= ancho_L:
        elemento = L[indice_inicial:indice_inicial + n]
        resultado.append(elemento)
        indice_inicial += 1
    return resultado
        