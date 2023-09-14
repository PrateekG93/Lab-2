#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 14:39:34 2023

@author: prateekgoswami
"""

I= int(input("Enter the monthly installment: "))     #take monthly installment
T = int(input("Enter the time you want to continue your RD(in months): "))   #take duration of RD
Total_return= I*(1+(7.1/100))**(12*(T/12))
#monthly insallment and duration should atleast Rs 500 and 6 respectively
if I>=500:
    if T>=6:
        print("Return of the RD will be Rs", Total_return)
    else:
        print("Enter period should be atleast 6 months")
else:
    print("Monthly installment should be atleast Rs 500")
    