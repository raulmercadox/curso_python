# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 14:49:20 2019

@author: ezmerra
"""

class myDict(object):
    """ Implements a dictionary without using a dictionary """
    def __init__(self):
        """ initialization of your representation """
        self.keys = []
        self.values = []
        
    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        if not k in self.keys:
            self.keys.append(k)
            self.values.append(v)
        else:
            indice = self.keys.index(k)
            self.values[indice] = v
        
    def getval(self, k):
        """ k, immutable object  """
        if k in self.keys:
            indice = self.keys.index(k)
            return self.values[indice]
        else:
            raise KeyError('KeyError successfully raised')
            
    def delete(self, k):
        """ k, immutable object """   
        if k in self.keys:
            indice = self.keys.index(k)
            self.keys.remove(k)
            self.values.remove(self.values[indice])
        else:
            raise KeyError('KeyError successfully raised')