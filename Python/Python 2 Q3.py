#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 14:51:29 2023

@author: prateekgoswami
"""

x = int(input("Enter the number x: "))
y =  int(input("Enter the number y: "))
if y% x== 0:
    print("y is divisible by x")
elif x <0 or y<0:
    print("Invalid input")
else:
    print("y is not divisible by x")