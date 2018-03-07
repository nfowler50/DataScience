#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 18:08:32 2017

@author: nickfowler
"""
import math, random, proba, stats
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import linalgbera as la
import gradient_descent as sgd
from functools import partial, reduce


def scale(data_matrix):
    """returns means and standard deviations of each column"""
    num_rows, num_columns=la.shape(data_matrix)
    means=[stats.mean(la.get_c(data_matrix,j))
           for j in range(num_columns)]
    stdevs=[stats.std_dev(la.get_c(data_matrix, j))
            for j in range(num_columns)]
    return means, stdevs

def rescale(data_matrix):
    """rescales input so that each column has mean 0 and std dev 1"""
    means, stdevs=scale(data_matrix)
    
    def rescaled(i,j):
        if stdevs[j]>0:
            return (data_matrix[i][j] - means[j] )/stdevs[j]
        else:
            return data_matrix[i][j]
        
    num_rows, num_columns=la.shape(data_matrix)
    return la.makeM(num_rows, num_columns, rescaled)

def de_mean_matrix(A):
    nr, nc=la.shape(A)
    col_means,_=scale(A)
    return la.makeM(nr, nc, lambda i, j: A[i][j]-col_means[j])

def direction(w):
    mag=la.mag(w)
    return [w_i/mag for w_i in w]

def directional_var_i(x_i,w):
    """variance of x_i in direction w"""
    return la.dot(x_i,direction(w))**2

#X is the de-meaned matrix

def directional_var(X,w):
    return sum(directional_var_i(x_i,w)
               for x_i in X)
    
def dir_var_grad_i(x_i,w):
    proj_length=la.dot(x_i,direction(w))
    return [2*proj_length*x_ij for x_ij in x_i]

def dir_var_grad(X,w):
    return la.vec_sum(dir_var_grad_i(x_i,w)
                      for x_i in X)
    
def first_prin_com(X):
    guess=[1 for _ in X[0]]
    unscaled_maximizer=sgd.maximize_batch(
           partial(directional_var, X),
           partial(dir_var_grad, X),
           guess)
    return direction(unscaled_maximizer)

def project(v,w):
    projection_length=la.dot(v,w)
    return la.sca_mult(projection_length, w)

def rem_proj_from_vec(v,w):
    return la.vec_sub(v,project(v,w))

def rem_proj(X,w):
    #for eachrow of X, project row onto w and subtract the result fro mthe row
    return [rem_proj_from_vec(x_i,w) for x_i in X]
    
#once we've removed projection from the data (imagine 2D) it's essentially 
#removed one of the dimensions. Just repeat the process of finding a principal
#axis and you've got the second prin axis!
    
def prin_com_ana(X, num_components):
    #this iteratively finds the prin axes
    components=[]
    for _ in range(num_components):
        component=first_prin_com(X)
        components.append(component)
        X=rem_proj(X,component)
        
    return components
        
def transform_vec(v, components):
    return [la.dot(v,w) for w in components]

def transform(X, components):
    return [transform_vec(x_i, components) for x_i in X]
    
    
    

    
