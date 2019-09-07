# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 21:56:09 2019

@author: ezmerra
"""
balance = 320000
annualInterestRate = 0.2
# expected result: Lowest Payment: 310

def calculateNewBalance(actualBalance, payment, monthlyInterestRate):
    pendingPayment = actualBalance - payment
    interest = monthlyInterestRate * pendingPayment
    newBalance = pendingPayment + interest
    return newBalance

monthlyRate = annualInterestRate / 12
minimumPayment = balance / 12
maximumPayment = (balance * (1 + annualInterestRate/12)**12) / 12

while True:
    newBalance = balance
    payment = (minimumPayment + maximumPayment)/2
    monthNumber = 1
    
    while monthNumber <= 12:
        newBalance = calculateNewBalance(newBalance, payment, monthlyRate)
        monthNumber += 1
        
    if newBalance > -0.01 and newBalance <= 0:
        break
    else:
        if newBalance > 0:
            minimumPayment = payment
        else:
            maximumPayment = payment
            
print("Lowest Payment:", round(payment, 2))
        
        


