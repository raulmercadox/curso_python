# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 21:05:56 2019

@author: ezmerra
"""

"""
Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + 
                             (Monthly interest rate x Monthly unpaid balance)
"""
balance = 320000
annualInterestRate = 0.2
# expected result: Lowest Payment: 310

def calculateNewBalance(actualBalance, payment, monthlyInterestRate):
    pendingPayment = actualBalance - payment
    interest = monthlyInterestRate * pendingPayment
    newBalance = pendingPayment + interest
    return newBalance

fixedPayment = 0
finalBalance = balance
while finalBalance > 0:
    finalBalance = balance
    fixedPayment += 10
    monthNumber = 0
    while monthNumber < 12:
        finalBalance = calculateNewBalance(finalBalance, fixedPayment, annualInterestRate/12)
        monthNumber += 1

print("Lowest Payment:", fixedPayment)

    
    
