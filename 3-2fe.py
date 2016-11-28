# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 01:29:55 2016

@author: sergeys04

Program that prints the sum of the numbers in s

"""

s = '1.21,35.2,54.43,58.9'
string = ''
total = 0
for x in s:
    if x != ',':
        string = string + x
    elif x == ',':
        total = total + float(string)
        string = ''
else:
    if len(string) > 0:
        total = total + float(string)
print (total)
