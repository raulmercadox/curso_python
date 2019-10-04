# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 19:16:15 2019

@author: ezmerra
"""

def genPrimes():
    list_primes = []
    candidate = 1
    while True:
        candidate += 1
        is_prime = True
        for number in list_primes:
            if candidate % number == 0:
                # It is not prime
                is_prime = False
                break
        if is_prime:
            list_primes.append(candidate)
            yield candidate
                
