#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 10:18:25 2017

@author: nickfowler
"""

from __future__ import division
from collections import Counter
import math, random
import matplotlib.pyplot as plt
import numpy as np
import proba
from mpl_toolkits.mplot3d import axes3d
import linalgbera as la

x,y = np.mgrid[-3:3:0.1, -3:3:0.1]

#V = (x+3)**2+(y-1)**2 # just a random function for the potential

V=np.sin(x)+np.cos(y)
#Ex=2*(x+3)
Ex,Ey=np.gradient(V)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot a basic wireframe.
ax.plot_wireframe(x, y, V)

#plt.figure()
#plt.quiver(x,y,Ex,Ey)

plt.show()


def step(v,direction,step_size):
    return[v_i+step_size*direction_i
           for v_i, direction_i in zip(v,direction)]

def sum_sqrs_gradient(v):
    return [2*v_i for v_i in v]
''' #the following statement finds the minimum sum of squares vector <0,0,0>
v=[random.randint(-10,10) for i in range(3)]

tolerance=0.0000001

while True:
    gradient=sum_sqrs_gradient(v)
    next_v=step(v,gradient,-0.01)
    if la.dis(next_v,v)<tolerance:
        break
    v=next_v

print (v)
'''

#stochastic gradient descent works when error functions are additive

def rand_order(data):
    #returns elements of data set in random order
    indexes=[i for i, _ in enumerate(data)]
    random.shuffle(indexes)
    for i in indexes:
        yield data[i]
        
def minimize_stochastic(target_fn,gradient_fn,x,y,theta_0,alpha_0=0.01):
    data=zip(x,y)
    theta=theta_0
    alpha=alpha_0
    min_theta,min_value=None,float("inf")
    iterations_with_no_improvement=0
    
    while iterations_with_no_improvement<100:
        value=sum(target_fn(x_i,y_i,theta) for x_i,y_i in data)
        
        if value<min_value:
            min_theta,min_value=theta,value
            iterations_with_no_improvement=0
            alpha=alpha_0
            
        else:
            iterations_with_no_improvement +=1
            alpha *=0.9
            
        for x_i,y_i in rand_order(data):
            gradient_i = gradient_fn(x_i,y_i,theta)
            theta=la.vec_sub(theta,la.sca_mult(alpha,gradient_i))
    
    return min_theta

def maximize_stochastic(target_fn,gradient_fn,x,y,theta_0,alpha_0=0.01):
    return minimize_stochastic(negate(target_fn),
                               negate_all(gradient_fn),
                               x,y,theta_0,alpha_0)

           
        
    
    
    