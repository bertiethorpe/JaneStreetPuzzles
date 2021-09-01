#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 05:59:55 2021

@author: bertiethorpe
"""

import numpy as np

def tugofwar():
    s = -0.28500012
    for n in np.arange(0,1000):
        s = s + ((-1)**n) * np.random.random()
        if (abs(s)>0.5):
            break    
    return np.sign(s)

iterable = (tugofwar() for i in np.arange(1000000))
array = np.fromiter(iterable,float)
mean = np.mean(array)

print(mean)