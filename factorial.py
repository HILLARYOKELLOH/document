# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 17:14:45 2020

@author: user
"""

n=int(input("enter a number"))
factorial=1
while n>0:
    factorial=factorial*n
    n=n-1
    print('factorial is',factorial)