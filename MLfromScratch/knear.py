#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 12:54:16 2017

@author: root
"""
from collections import Counter
import linalgbera as la

def raw_majority_vote(labels):
    votes=Counter(labels)
    winner, _ =votes.most_common(1)[0]
    return winner

def majority_vote(labels):
    """assumes labels are ordered nearest to farthest"""
    vote_counts=Counter(labels)
    winner, winner_count=vote_counts.most_common(1)[0]
    num_winners=len([count
                     for count in vote_counts.values()
                     if count==winner_count])
    if num_winners==1:
        return winner
    else:
        return majority_vote(labels[:-1]) #remove farthest and try again
    
def knn_classify(k, labeled_points, new_point):
    by_dis=sorted(labeled_points,
                  key=lambda point_label: la.dis(point_label[0], new_point))   
    k_nearest_labels=[label for _, label in by_dis[:k]]
    return majority_vote(k_nearest_labels)


    


