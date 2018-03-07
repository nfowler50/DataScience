#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 12:11:14 2017

@author: nickfowler
"""
from matplotlib import pyplot as plt
from collections import Counter
'''
years=[1950,1960,1970,1980,1990,2000,2010]
gdp=[300.2,543.3, 1075.9,2862.5,5979.6,10289.7,14958.3]

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
plt.title("Nominal GDP")
plt.ylabel("Billions of $")
'''
 
'''
movies=["dgfafb","sbfd","argreh","afg","das"]
num=[3,6,2,7,4]

xd=[i+0.1 for i, _ in enumerate(movies)]

plt.bar(xd, num)
plt.title("goop")

plt.xticks([i+0.1 for i, _ in enumerate(movies)], movies)
'''
'''
grades=[34,56,34,45,67,12,34,56,86,89,90,34,56]
decile=lambda grade: grade // 10*10
histogram=Counter(decile(grade) for grade in grades)
plt.bar([x-4 for x in histogram.keys()],
         histogram.values(),
         8)
plt.axis([-5,105,0,5])
'''
'''
mentions=[500,505]
years=[2013,2014]

plt.bar([2012.6, 2013.6],mentions, 0.8)
plt.xticks([2012.6, 2013.6], ["2013","2014"])
plt.ticklabel_format(useOffset=False)
plt.axis([2012.5,2014, 499, 506])
'''
'''
variance=[1,2,4,8,16,32,64,128,256]
bias_sqd=[256,128,64,32,16,8,4,2,1]
total_er=[x+y for x,y in zip(variance,bias_sqd)]
xs=[i for i, _ in enumerate(variance)]

plt.plot(xs, variance, 'g-', label=('variance'))
plt.plot(xs, bias_sqd, 'r-.', label=('bias'))
plt.plot(xs, total_er, 'b:', label=('total err'))

plt.legend(loc=9)
'''
friends=[70,62,34,57,99,101]
minutes=[120,170,29,135,153,200]
labels=['a','b','c','d','e','f']

plt.scatter(friends, minutes)
for label, frnd_cnt, min_cnt in zip(labels,friends,minutes):
    plt.annotate(label,
                 xy=(frnd_cnt,min_cnt),
                 xytext=(5,-5),
                 textcoords='offset points')
