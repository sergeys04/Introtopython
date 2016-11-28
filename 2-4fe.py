# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 13:00:26 2016

@author: sergeys04

Find the largest odd number from a list of integers
"""
alist = []
blist = []
while len(alist) <= 10:
    num = int(input("Enter a number: "))
    alist.append(num)
    if num % 2 != 0:
        blist.append(num)
print ('The largest odd number is: ', max(blist))