# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 23:25:23 2016

@author: sergeys04

Find pwr and root so that root**pwr is equal to x, 0 < root < 7

"""

x = int(input("Enter an integer: "))
root = 1
pwr = 2
while root ** pwr < abs(x):
    root += 1
    if root ** pwr > abs(x) and root < 7:
        root = 1
        pwr += 1
    elif root ** pwr > abs(x) and root > 6:
        print ('Error message')        
        break
else:
    print ('root:', root,'pwr:', pwr)