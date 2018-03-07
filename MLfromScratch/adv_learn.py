#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 18:55:32 2017

@author: nickfowler
"""
from collections import Counter
import matplotlib.pyplot as plt
from collections import defaultdict
import random
from functools import partial

x=[4,6,3,7,9]
y=sorted(x)
print(y)
print(x)

x.sort()
print(x)

x=sorted([-4,5,2,-1], key=abs, reverse=True)
print (x)

even_numbers=[x for x in range(5) if x%2==0]
squares=[x*x for x in range(5)]
even_squares=[x*x for x in even_numbers]

print(even_numbers,
      squares,
      even_squares)

square_dict={x:x*x for x in range(5)}
square_set={x*x for x in [-1,1]}

print(square_dict)
print(square_set)



pairs=[(x,y) for x in range(10) for y in range(10)]
print(pairs)

#plt.plot()

#xs=[j[0] for j in pairs]
#ys=[j[1] for j in pairs]
#plt.scatter(xs, ys)


increasing_pairs=[(x, y)
for x in range(10)
for y in range(x+1,10)]

print (increasing_pairs)

xs, ys = zip(*pairs)

#xs=[j[0] for j in increasing_pairs]
y#s=[j[1] for j in increasing_pairs]
#plt.scatter(xs, ys)

relate=defaultdict(int)
relate={j[0] : j[1] for j in increasing_pairs}

def lazy_range(n):
    i=0
    while i<n:
        yield i
        i+=1
        
for i in lazy_range(10):
    print(i)

print(relate.items())

uni_randos=[random.random() for _ in range(4)]
print(uni_randos)

print(random.randrange(10))

def exp(base, power):
    return base**power

two_to=partial(exp,power=2)
print (two_to(5))

def double(x):
    return 2*x
xt=[1,2,3,4,5,6,7,8]
#doubles=[double(x) for x in xt]
#doubles=list(map(double, xt))
#print(doubles)
ldbl=partial(map,double)
ldbl(xt)
print (list(ldbl(xt)))

def is_even(x):
    return x%2==0

#x_evens=[x for x in xt if is_even(x)]
x_evens=list(filter(is_even,xt))
print(x_evens)

documents="bleh broo beep boop bop dubby doop"
document=documents.split()
for i, d in enumerate(document):
    print (i,d)
    
def magic(*args, **kwargs):
    print ("args: ", args)
    print ("kwargs: ", kwargs)

magic(1,2,3, key='dfg')