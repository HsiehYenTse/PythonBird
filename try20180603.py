#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 17:09:03 2018

@author: xieyanduo
"""
import numpy as np
import math
import csv

w = np.load('model.npy')

test_x = []
    
with open('test.csv', 'r', encoding = 'big5') as csvfile:
    text = csv.reader(csvfile, delimiter = ',')
    i = 0
    j = -1
    for row in text:
        if (i%18) == 0:
            j = j + 1
            test_x.append([])
        for k in range(2, 11):
            if row[k] != 'NR':
                test_x[j].append(float(row[k]))
            else:
                test_x[j].append(float(0))        
        i = i + 1

test_x = np.array(test_x)

#adding bias
test_x = np.concatenate((np.ones([test_x.shape[0], 1]), test_x), axis = 1)
ans = []
for i in range(len(test_x)):
   ans.append(['id_'+str(i)])
   a = np.dot(w, test_x[i])
   ans[i].append(a)
   
filename = 'predict1.csv'   
with open(filename, 'w+') as text:
    o = csv.writer(text, delimiter = ',', lineterminator = '\n')
    o.writerow(['id', 'value'])
    for row in ans:
        o.writerow(row)


      