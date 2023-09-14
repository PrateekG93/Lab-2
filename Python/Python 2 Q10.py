#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 22:56:38 2023

@author: prateekgoswami
"""

num= int(input("Enter a number between 1 to 86400: "))
hours= num//3600
minutes= (num- (hours*3600))//60
sec= num- (hours*3600)- (minutes*60)
print(hours,"hours", minutes,"minutes", sec,"seconds")