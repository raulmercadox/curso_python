# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 12:49:40 2019

@author: ezmerra
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthNumber = 0

def calculateNewBalance(actualBalance, payment, monthlyInterestRate):
    pendingPayment = actualBalance - payment
    interest = monthlyInterestRate * pendingPayment
    newBalance = pendingPayment + interest
    return newBalance

while monthNumber < 12:
    payment = balance * monthlyPaymentRate
    balance = calculateNewBalance(balance, payment, annualInterestRate/12)
    monthNumber += 1

print(round(balance, 2))