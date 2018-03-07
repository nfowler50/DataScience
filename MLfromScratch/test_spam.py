#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 20:01:07 2017

@author: root
"""

import spam_filter as sf
import glob, re, random
from collections import Counter

path=r"/root/Documents/DatA/spam/*/*"

data=[]
for fn in glob.glob(path):
    is_spam="ham" not in fn
    
    with open(fn, 'r',encoding='ISO-8859-1') as file:
        for line in file:
            if line.startswith("Subject:"):
                subject=re.sub(r"^Subject: ", "",line).strip()
                data.append((subject, is_spam))
    
def split_data(data, prob):
    """split data into fractions [prob, 1 - prob]"""
    results = [], []
    for row in data:
        results[0 if random.random() < prob else 1].append(row)
    return results
    
train_data, test_data = split_data(data, 0.75)

classifier=sf.NaiveBayes()
classifier.train(train_data)
#trips -> subject, acutal spam, predicted spam prob
classified=[(subject, is_spam, classifier.classify(subject))
            for subject, is_spam in test_data]

counts=Counter((is_spam, spam_probability>0.75,)
                for _, is_spam, spam_probability in classified)

print(counts)





