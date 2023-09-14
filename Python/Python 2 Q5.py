#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 15:05:01 2023

@author: prateekgoswami
"""

Pie= 3.142
r= float(input("Enter the radius: "))
area = Pie*r**2
if r<100 and r>0:
    print("Area", area)
else :
    print("Radius is not valid")