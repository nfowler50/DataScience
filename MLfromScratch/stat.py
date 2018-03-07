#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 18:17:57 2017

@author: nickfowler
"""

import linalgbera as la
import matplotlib.pyplot as plt
from collections import Counter
import math
from math import sqrt

def mean(x):
    n=len(x)
    return (sum(x)/n)

def median(vals):
    sorted_vals=sorted(vals)
    n=len(vals)
    mid=n//2
    if n%2==1:
        return sorted_vals[mid]
    else:
        lo=mid-1
        hi=mid
        return (sorted_vals[hi]+sorted_vals[lo])/2
    
def quantile(x, p):
    p_in=int(p*len(x))
    return sorted(x)[p_in]

def mode(x):
    counts=Counter(x)
    maxc=max(counts.values())
    return [xi for xi, count in counts.items() if count==maxc]

def demean(x):
    xbar=mean(x)
    return [xi-xbar for xi in x]

def variance(x):
    n=len(x)
    dev=demean(x)
    return (la.sum_sqrs(dev)/(n-1))

def std_dev(x):
    return sqrt(variance(x))

def covariance(x,y):
    n=len(x)
    return la.dot(demean(x),demean(y))/(n-1)

def correlation(x,y):
    stdevX=std_dev(x)
    stdevY=std_dev(y)
    if stdevX>0 and stdevY>0:
        return covariance(x,y)/stdevX/stdevY
    else:
        return 0