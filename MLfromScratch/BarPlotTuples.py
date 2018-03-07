#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 15:48:29 2017

@author: nickfowler
"""
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

top=[('trump', 15), ('veteransday', 10), ('roymoorechildmolester', 8), ('maga', 5), ('periscope', 4), ('news', 4), ('russia', 3), ('trump2020', 3), ('needtoimpeach', 3), ('bitcoin', 2)]

topic, posts=zip(*top)

plt.bar(range(len(topic)), posts, align='center')
plt.xticks(np.arange(len(topic)), topic, rotation=45, ha='right')
plt.ylabel('# of posts')

