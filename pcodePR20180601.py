#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 20:06:12 2018

@author: xieyanduo
"""

list1 = [1, 2, 3, 4, 5, '6', '7', 8., 9., 10.]

#print('list1 =', list1 )
#print(type(list1))
#print(list1[-4:])

#list1[0:2] = [] # [] means nothing, nothing means nothing 
#print(list1) 

#so if I want to clear all the datas of a list, type-> list[:] = []

#def ask_name(usr_name = '', retries = 4, complaint = 'why not just enter your fucking name:'):
#    print(complaint)
#    while True:
#        usr_name = input()
#        if usr_name in ('paul', 'pig', 'ass'):
#            print('this name is unavailible')
#        elif usr_name != '':
#            print('Hi,', usr_name)
#            return False
#        if retries <= 0:
#            raise OSError('Uncooperative User!')
#        print(complaint)
#        retries = retries - 1       
#
#ask_name(complaint = 'Please enter your name', retries = 2)

i = 1
def apig(a, pg = None):
    if pg == None:
        pg = []
    pg.append(a)
    print(pg)
i = 2

apig(i)
apig(i)
apig(i)

a = [1, 2, 3] #list type

#b = a

#b = []
#for i in a:
#    b.append(i)

b = []
b.extend(a)
b[0] = 's'
print(a, b)
def fucku():
    '''
    go fuck yourself
    '''
    pass

print(fucku.__doc__)
print(apig.__annotations__)






