#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title - Decision tree

Created on Wed Aug 14 04:59:09 2019
@author: k as root
"""

from sklearn import tree

#[height , weight, shoe size]
X = data # generated from the commented code below
Y = ['male', 'female', 'female', 'female', 'male', 'male', 'male',
     'female', 'male', 'female']

# DecisionTreeClassifier
clf = tree.DecisionTreeClassifier()
clf.fit(X,Y)
prediction = clf.predict([[192,70,43]])
print(prediction)

#TODO:
# 1. Use any 3 scikit-learn models on this dataset
# 2. Compare results
# 3. Print the best one


""" ------< Generate random numbers
from random import randrange 
rnum = list()
for i in range(10):
    #print(randrange(154,181))
    rnum.append(randrange(37,44))
print(rnum)

#----------< structure the data >
import numpy as np
from scipy import linalg, sparse

d = [c1,c2,c3]
dd = np.array(d)
data = dd.T
print(data)

DATA:
[[166  76  42]
 [167  66  37]
 [174  83  40]
 [155  64  39]
 [170  58  40]
 [172  60  40]
 [173  68  38]
 [174  67  39]
 [166  64  38]
 [160  59  41]]
"""
