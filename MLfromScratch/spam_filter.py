# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from collections import defaultdict
import re, math

def tokenize(message):
    message=message.lower()
    all_words=re.findall("[a-z0-9']+",message)
    return set(all_words)

def count_words(training_set):
    counts=defaultdict(lambda: [0,0])
    for message, is_spam in training_set:
        for word in tokenize(message):
            counts[word][0 if is_spam else 1]+=1
    return counts

def word_probabilities(counts, total_spams, total_non_spams, k=0.5):
    return [(w,
             (spam+k)/(total_spams+2*k),
             (non_spam+k)/(total_non_spams+2*k))
            for w, (spam, non_spam) in counts.items()]
    
def spam_probability(word_probs, message):
    message_words=tokenize(message)
    log_pspam=log_pnotspam=0.0
    for word, pspam, pnotspam in word_probs:
        if word in message_words:
            log_pspam += math.log(pspam)
            log_pnotspam += math.log(pnotspam)
        else:
            log_pspam += math.log(1-pspam)
            log_pnotspam += math.log(1-pnotspam)
            
    pspam=math.exp(log_pspam)
    pnotspam=math.exp(log_pnotspam)
    
    return pspam/(pspam + pnotspam)


class NaiveBayes:
    def __init__(self, k=0.5):
        self.k=k
        self.word_probs=[]
        
    def train(self, training_set):
        num_spams=len([is_spam
                       for message, is_spam in training_set
                       if is_spam])
        num_nspams=len(training_set)-num_spams
        
        word_counts=count_words(training_set)
        self.word_probs=word_probabilities(word_counts,
                                           num_spams,
                                           num_nspams,
                                           self.k)
        
    def classify(self, message):
        return spam_probability(self.word_probs, message)
    
    
    
    
    
    
    
    


