#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:02:45 2017

@author: nickfowler
"""
import math, proba, random, csv, dateutil.parser
from collections import Counter, defaultdict
import matplotlib.pyplot as plt
import numpy as np

def bucketize(point, bucket_size):
    return bucket_size * math.floor(point / bucket_size)

def make_histogram(points, bucket_size):
    return Counter(bucketize(point, bucket_size) for point in points)

def plot_histogram(points, bucket_size, title=" "):
    histogram=make_histogram(points, bucket_size)
    plt.bar(list(histogram.keys()), list(histogram.values()), width=bucket_size)
    plt.title(title)
    plt.show()
    
    
#random.seed(0)
'''
uniform=[200*random.random()-100 for _ in range(10000)]

normal=[57*proba.inv_normalcdf(random.random())
        for _ in range(10000)]

plot_histogram(uniform, 1, "uniform histogram")
plot_histogram(normal, 1, "normal histogram")
'''
def random_normal():
    return proba.inv_normalcdf(random.random())

xs=[random_normal() for _ in range(1000)]
ys1=[x+random_normal()/2 for x in xs]
ys2=[-x+random_normal()/2 for x in xs]

plot_histogram(ys1, .5, "x+rand")
plot_histogram(ys2, .5, "-x+rand")

plt.scatter(xs, ys1, marker='.', color='black', label='ys1')
plt.scatter(xs, ys2, marker='.', color='grey', label='ys2')


r1=np.corrcoef([xs, ys1, ys2]) 
#r2=np.corrcoef(xs, ys2)
print(r1)

'''
def parse_row(input_row, parsers):
    return[parser(value) if parser is not None else value
           for value, parser in zip(input_row, parsers)]
'''






