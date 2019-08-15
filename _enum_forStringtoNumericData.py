#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 21:14:10 2019

@author: k as root
"""

# Prototype for converting strings to numeric values

from enum import Enum

class Color(Enum):
    red = 1
    green = 2
    blue = 3

# Check----->>
#print(Color.red)
#print(Color(1))
#print(Color['red'])
    
[c for c in Color]  # iterate