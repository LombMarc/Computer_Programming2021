#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 13:55:36 2021

@author: marcolombardi
"""
import math
import random

def trip_fact(n):
    ls=[n]
    i=n
    while i >1:
        ls.append(i-3)
        i-=3
    tf=1
    for j in ls:
        tf=tf*j
    return tf,ls
#print(trip_fact(22)[1][0:3])

def twoLs(M,N):
    tf=trip_fact(N)[0]
    tripl_List=trip_fact(N)[1]
    tripl_List[0:M]
    rand_List=[]
    for i in range(tf):
        ls2.append(random.randint(1, tf))
    return ls1,ls2
    
def mergeRandom(lt,lr):
    lf=[]
    for i in range(len(lt)):
        if lr[i]>lt[i]:
            lf.append(lr[i])
            lf.append(lt[i])
        else:
            lf.append(lt[i])
    return lf

#print(mergeRandom([0,1,2,3,4,10,18,21], [5,3,4,6,9,20,12,22]))


