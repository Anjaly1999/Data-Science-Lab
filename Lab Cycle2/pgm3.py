#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 12:20:39 2021

@author: sjcet
"""

import numpy as np

print("an uninitialized array :")
print(np.empty([2,2]))
print("array with all elements as 1 :")
print(np.full([2,2],1))
print("all elements as 0 :")
print(np.zeros([2,2]))