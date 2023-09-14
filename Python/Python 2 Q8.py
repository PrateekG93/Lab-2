#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 15:31:51 2023

@author: prateekgoswami
"""

year = int(input("Enter the year: "))
if year%4==0 and year%100!=0:
    print("It is a leap year")
elif year%400==0:
    print("It is a leap year")
else:
    print("It is not a leap year")
    