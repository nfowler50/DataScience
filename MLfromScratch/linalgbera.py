#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 17:14:00 2017

@author: nickfowler
"""

from functools import reduce
from math import sqrt

def vec_add(v,w):
    return[vi+wi for vi,wi in zip(v,w)]

def vec_sub(v,w):
    return[vi-wi for vi,wi in zip(v,w)]

'''    
def vec_sum(vectors):
    result=vectors[0]
    for vector in vectors[1:]:
        result=vec_add(result,vector)
    return result
'''
def vec_sum(vectors):
    return reduce(vec_add, vectors)

def sca_mult(a,v):
    return[a*vi for vi in v]
    
def vec_mean(vectors):
    n=len(vectors)
    return sca_mult(1/n,vec_sum(vectors))

def dot(v,w):
    return sum(vi*wi for vi,wi in zip(v,w))
    
def sum_sqrs(v):
    return dot(v,v)

def mag(v):
    return sqrt(sum_sqrs(v))

def sq_dis(v,w):
    return sum_sqrs(vec_sub(v,w))

def dis(v,w):
    return mag(vec_sub(v,w))

def shape(A):
    num_r=len(A)
    num_c=len(A[0]) if A else 0
    return (num_r,num_c)

def get_r(A,i):
    return A[i]

def get_c(A,j):
    return [Ai[j] for Ai in A]

def makeM(num_r, num_c, entry_fn):
    return[[entry_fn(i,j) for j in range(num_c)] for i in range(num_r)]

def ident(i,j):
    return 1 if i==j else 0


    
#test=mag([1,2,3])
#test=dis([1,2,3],[3,4,5])
#test=sca_mult(3,[1,2,3])

#print(test)