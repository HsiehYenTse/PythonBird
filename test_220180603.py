#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 17:45:27 2018

@author: xieyanduo
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 14:19:56 2018

@author: xieyanduo
LeeML homework
"""

import csv 
import numpy as np
from numpy.linalg import inv
import random
import math
import sys

#data = []
## 每一個維度儲存一種污染物的資訊
#for i in range(18):
#	data.append([])
#
#n_row = 0
#text = open('train.csv', 'r', encoding='big5')
#row = csv.reader(text , delimiter=",")
#for r in row:
#    # 第0列沒有資訊
#    if n_row != 0:
#        # 每一列只有第3-27格有值(1天內24小時的數值)
#        for i in range(3,27):
#            if r[i] != "NR":
#                data[(n_row-1)%18].append(float(r[i]))
#            else:
#                data[(n_row-1)%18].append(float(0))	
#    n_row = n_row+1
#text.close()
#
#x = []
#y = []
## 每 12 個月
#for i in range(12):
#    # 一個月取連續10小時的data可以有471筆
#    for j in range(471):
#        x.append([])
#        # 18種污染物
#        for t in range(18):
#            # 連續9小時
#            for s in range(9):
#                x[471*i+j].append(data[t][480*i+j+s] )
#        y.append(data[9][480*i+j+9])
#x = np.array(x)
#y = np.array(y)
data = []
for i in range(18):
    data.append([])
    
with open('train.csv', 'r', encoding = 'big5') as csvfile:
    text = csv.reader(csvfile, delimiter = ',')
    i = 0
    for row in text:                #讀取ＤＡＴＡ
        if i != 0:
            for j in range(3, 27):
                if row[j] != 'NR':
                    data[(i-1)%18].append(float(row[j]))  #記得要換成float，不然原本是str
                else:
                    data[(i-1)%18].append(float(0))
        i = i + 1


#data = np.transpose(data) #transpose to an matrix
x = []
y = []
for i in range(12):                #生成training pairs
    for j in range(471):     
        x.append([])
        for k in range(18):
            for m in range(9):
                x[i*471+j].append(data[k][i*24*20+j+m])
        y.append(data[9][i*24*20+j+m+1])

x = np.array(x)
y = np.array(y)

# add square term
# x = np.concatenate((x,x**2), axis=1)

#這邊記得加入bias，把原本x矩陣最左邊再加入一行
#x = np.concatenate((np.ones((x.shape[0],1)),x), axis=1)
x = np.concatenate((np.ones([len(x.T[0]), 1]), x),axis = 1)
w = np.zeros(162+1)   #w = weight, total 18(測項)*9(9小時當作一組features)=162+bias=163, 163*1的矩陣 
x_t = x.transpose()
s_grad = np.zeros(len(x[0]))
l_rate = 10
iterations = 10000

for i in range(iterations):
    t_y = np.dot(x, w) 
    loss = t_y - y
    cost = np.sum(loss**2) / len(x)
    cost_avg = math.sqrt(cost)      #去看每一次迭代，平均誤差（cost_avg）應該是要越來越小的
    
    grad = np.dot(x_t, loss)    #
    s_grad += grad**2
    ada = np.sqrt(s_grad)
    w = w - l_rate * grad / ada
    print('iterations: %d | cost: %f ' %(i, cost_avg))  
    
    
# save model
np.save('model1.npy',w)
# read model
w = np.load('model1.npy')

test_x = []
n_row = 0
text = open('test.csv' ,"r")
row = csv.reader(text , delimiter= ",")

for r in row:
    if n_row %18 == 0:
        test_x.append([])
        for i in range(2,11):
            test_x[n_row//18].append(float(r[i]) )
    else :
        for i in range(2,11):
            if r[i] !="NR":
                test_x[n_row//18].append(float(r[i]))
            else:
                test_x[n_row//18].append(0)
    n_row = n_row+1
text.close()
test_x = np.array(test_x)

# add square term
# test_x = np.concatenate((test_x,test_x**2), axis=1)

# add bias
test_x = np.concatenate((np.ones((test_x.shape[0],1)),test_x), axis=1)

ans = []
for i in range(len(test_x)):
    ans.append(["id_"+str(i)])
    a = np.dot(w,test_x[i])
    ans[i].append(a)

filename = "predict.csv"
text = open(filename, "w+")
s = csv.writer(text,delimiter=',',lineterminator='\n')
s.writerow(["id","value"])
for i in range(len(ans)):
    s.writerow(ans[i]) 
text.close()