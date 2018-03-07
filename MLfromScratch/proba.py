#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 08:43:37 2017

@author: nickfowler
"""
from __future__ import division
from collections import Counter
from scipy.stats import norm
import math, random
import matplotlib.pyplot as plt
import numpy as np

xs=[]
ys=[]

def uniformd(x):
    return 1 if x>=0 and x<1 else 0

def uniformcdf(x):
    if x<0: return 0
    elif x<1:return x
    else: return 1
    
def normalpdf(x, mu=0, sigma=1):
    rtpi=math.sqrt(2*math.pi)
    return(math.exp(-(x-mu)**2/2/sigma**2)/(rtpi*sigma))
    
def normalcdf(x,mu=0,sigma=1):
    return (1+math.erf((x-mu)/math.sqrt(2)/sigma))/2

'''
def inv_normalcdf(p,mu=0,sigma=1,tolerance=0.0001):
    if mu!= 0 or sigma!=1:
        return mu+sigma*inv_normalcdf(p, tolerance=tolerance)
    
    low_z=-10
    high_z=10
    while high_z-low_z > tolerance:
        mid_z=(high_z+low_z)/2
        mid_p=normalcdf(mid_z)
        if mid_p<p: #midpoint still too low
            low_z=mid_z
        elif mid_p>p: #midpoint still too high
            high_z=mid_z
        else:
            break
        
    return mid_z
 '''
def inv_normalcdf(p,mu=0,sigma=1):
    return norm.ppf(p,mu,sigma)

def bernoulli(p):
    return 1 if random.random() <p else 0

def binomial(n,p):
    return sum(bernoulli(p) for _ in range(n))

def make_hist(p,n,num_pts):
    data=[binomial(n,p) for _ in range(num_pts)]
    histogram=Counter(data)
    
    plt.bar([x-0.4 for x in histogram.keys()],[v/num_pts for v in histogram.values()],0.8,color='0.75')
    
    mu=p*n
    sigma=math.sqrt(n*p*(1-p))
    
    xs=range(min(data),max(data)+1)
    ys=[normalcdf(i+0.5,mu,sigma)-normalcdf(i-0.5,mu,sigma) for i in xs]
    
def normal_appro_bino(n,p):
    mu=p*n
    sigma=math.sqrt(p*(1-p)*n)
    return mu, sigma

def prob_above_cdf(lo, mu=0, sigma=1):
    return 1-normalcdf(lo,mu,sigma)

def prob_between(lo,hi,mu=0,sigma=1):
    return normalcdf(hi,mu,sigma)-normalcdf(lo,mu,sigma)

def prob_outside(lo,hi,mu=0,sigma=1):
    return 1-prob_between(lo,hi,mu,sigma)

def norm_up_bound(probability, mu=0, sigma=1):
    return inv_normalcdf(probability,mu,sigma)

def norm_low_bound(probability,mu=0,sigma=1):
    return inv_normalcdf(1-probability,mu,sigma)

def norm_two_bounds(probability, mu=0, sigma=1):
    tail_prob=(1-probability)/2
    up_bound=norm_low_bound(tail_prob,mu,sigma)
    low_bound=norm_up_bound(tail_prob,mu,sigma)
    
    return low_bound,up_bound
    
def two_sided_p_val(x, mu=0,sigma=1):
    if x>=mu:
        return 2*prob_above_cdf(x,mu,sigma)
    else:
        return 2*normalcdf(x,mu,sigma)
    
def B(alpha,beta):
    #normalizing constant to make tot prob 1
    return math.gamma(alpha)*math.gamma(beta)/math.gamma(alpha+beta)

def beta_pdf(x,alpha,beta):
    if x<=0 or x>=1:
        return 0
    return x**(alpha-1)*(1-x)**(beta-1)/B(alpha,beta)
    

