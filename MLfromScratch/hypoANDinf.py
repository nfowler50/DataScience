#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 08:40:13 2017

@author: nickfowler
"""
from __future__ import division
from collections import Counter
import math, random
import matplotlib.pyplot as plt
import numpy as np
import proba

mu_0,sigma_0=proba.normal_appro_bino(1000,0.5)
low, hi=proba.norm_two_bounds(0.95, mu_0, sigma_0)
print("reject if below:",low,"reject if above:",hi)

mu_1,sigma_1=proba.normal_appro_bino(1000,0.525)
type_2_probability=proba.prob_between(low,hi,mu_1,sigma_1)
power=1-type_2_probability

print("chance of type 2 error with 52.5% preference to heads:", power)

chance=proba.two_sided_p_val(531.5,mu_0,sigma_0)
chance2=proba.two_sided_p_val(468.5,mu_0,sigma_0)
print("chance of seeing outside distance from mean by val given:",chance2)

#let's compare this result to the results from a simulation. Lets simulate flipping a coin 1000 times and run the simulation 100,000 times
'''
extreme_val_cnt=0
for _ in range(100000):
    num_heads=sum(1 if random.random()< 0.5 else 0
                  for _ in range(1000))
    if num_heads >= 530 or num_heads <=470:
        extreme_val_cnt += 1
        
print(extreme_val_cnt/100000)
'''

upper_p=proba.prob_above_cdf(526.5, mu_0, sigma_0)
lower_p=proba.normalcdf(473.5, mu_0,sigma_0)

print("chance of seeing above hi val given:", upper_p)
print("chance of seeing below lo val given:", lower_p)

def run_experiment():
    return [random.random() < 0.5 for _ in range(1000)]

def reject_fairness(experiment):
    num_heads=len([flip for flip in experiment if flip])
    return num_heads<469 or num_heads>531

random.seed(0)
experiments=[run_experiment() for _ in range(1000)]
num_rejections=len([experiment for experiment in experiments
                    if reject_fairness(experiment)])
    
print(num_rejections)

def est_parameters(N,n):
    p=n/N
    sigma=math.sqrt(p*(1-p)/N)
    return p, sigma

def ab_test_stat(Na,na,Nb,nb):
    pa,sigma_a=est_parameters(Na,na)
    pb,sigma_b=est_parameters(Nb,nb)
    return(pb-pa)/math.sqrt(sigma_a**2+sigma_b**2)
    
z=ab_test_stat(1000,200,900,150)

prob=proba.two_sided_p_val(z)

print(z)
print(prob)

print(24/31)
    
    
    
