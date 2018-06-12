#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 14:18:01 2018

@author: xieyanduo
"""
import csv
import pandas as pd
import numpy as np
import math

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
        y.append(data[9][i*24*20+j+9])

x = np.array(x)
y = np.array(y)


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
    
np.save('model.npy', w)     #  ,w : 把w存進去
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
   
filename = 'predict.csv'   
with open(filename, 'w+') as text:
    o = csv.writer(text, delimiter = ',', lineterminator = '\n')
    o.writerow(['id', 'value'])
    for row in ans:
        o.writerow(row)


    
   
   



             


       
                
        

    
    
        

        


