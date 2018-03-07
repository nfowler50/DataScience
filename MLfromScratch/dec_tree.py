#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 13:19:46 2017

@author: root
"""
import math
from collections import Counter, defaultdict
from functools import partial


def entropy(class_probs):
    return sum(-p*math.log(p,2)
               for p in class_probs
               if p)
    
def class_probs(labels):
    total_cnt=len(labels)
    return [count/total_cnt
            for count in Counter(labels).values()]
    
def data_entropy(labeled_data):
    labels=[label for _,label in labeled_data]
    probs=class_probs(labels)
    return entropy(probs)

def partition_entropy(subsets):
    total_count=sum(len(subset) for subset in subsets)
    return sum(data_entropy(subset)*len(subset)/total_count
               for subset in subsets)
'''
def partition_by(inputs, attribute):
    groups=defaultdict(list)
    for inp in inputs:
        key=inp[0][attribute]
        groups(key).append(inp)
    return groups
'''
def group_by(items, key_fn):
    """returns a defaultdict(list), where each input item
    is in the list whose key is key_fn(item)"""
    groups = defaultdict(list)
    for item in items:
        key = key_fn(item)
        groups[key].append(item)
    return groups

def partition_by(inputs, attribute):
    """returns a dict of inputs partitioned by the attribute
    each input is a pair (attribute_dict, label)"""
    return group_by(inputs, lambda x: x[0][attribute])

def partition_entropy_by(inputs, attribute):
    partitions=partition_by(inputs, attribute)
    return partition_entropy(partitions.values())

def classify(tree, inp):
    if tree in [True, False]:
        return tree
    attribute, subtree_dict=tree
    
    subtree_key=inp.get(attribute)
    
    if subtree_key not in subtree_dict:
        subtree_key=None
        
    subtree=subtree_dict[subtree_key]
    return classify(subtree, inp)

def buildtree_id3(inputs, split_candidates=None):
    if split_candidates is None:
        split_candidates=inputs[0][0].keys()
        
    num_inputs=len(inputs)
    num_trues=len([label for item, label in inputs if label])
    num_falses=num_inputs-num_trues
    
    if num_trues==0: return False
    if num_falses==0: return True
    
    if not split_candidates:
        return num_trues>=num_falses
    
    best_attribute=min(split_candidates,
                       key=partial(partition_entropy_by, inputs))
    
    partitions=partition_by(inputs, best_attribute)
    new_candidates=[a for a in split_candidates
                    if a != best_attribute]
    
    '''    
    subtrees={attribute_value : buildtree_id3(subset, new_candidates)
              for attribute_value, subset in partitions.iteritems()}
    ''' 
    
    subtrees = { attribute : buildtree_id3(subset, new_candidates)
    for attribute, subset in partitions.items() }
    
    subtrees[None]=num_trues > num_falses
    
    return (best_attribute, subtrees)



if __name__ == "__main__":

    inputs = [
        ({'level':'Senior','lang':'Java','tweets':'no','phd':'no'},   False),
        ({'level':'Senior','lang':'Java','tweets':'no','phd':'yes'},  False),
        ({'level':'Mid','lang':'Python','tweets':'no','phd':'no'},     True),
        ({'level':'Junior','lang':'Python','tweets':'no','phd':'no'},  True),
        ({'level':'Junior','lang':'R','tweets':'yes','phd':'no'},      True),
        ({'level':'Junior','lang':'R','tweets':'yes','phd':'yes'},    False),
        ({'level':'Mid','lang':'R','tweets':'yes','phd':'yes'},        True),
        ({'level':'Senior','lang':'Python','tweets':'no','phd':'no'}, False),
        ({'level':'Senior','lang':'R','tweets':'yes','phd':'no'},      True),
        ({'level':'Junior','lang':'Python','tweets':'yes','phd':'no'}, True),
        ({'level':'Senior','lang':'Python','tweets':'yes','phd':'yes'},True),
        ({'level':'Mid','lang':'Python','tweets':'no','phd':'yes'},    True),
        ({'level':'Mid','lang':'Java','tweets':'yes','phd':'no'},      True),
        ({'level':'Junior','lang':'Python','tweets':'no','phd':'yes'},False)
]
    
    for key in ['level','lang','tweets','phd']:
        print(key, partition_entropy_by(inputs, key))

senior_inputs=[(inp, label)
               for inp, label in inputs if inp["level"]=='Senior']

print('\n')

for key in ['lang','tweets', 'phd']:
    print(key, partition_entropy_by(senior_inputs, key))

print('\n')

tree=buildtree_id3(inputs)

print(classify(tree, {'level':"Junior",
                'lang':'Java',
                'tweets':'yes',
                'phd':'no'}))
        
print(classify(tree, {'level':"Junior",
                'lang':'Java',
                'tweets':'yes',
                'phd':'yes'}))
        
        
        





    
    
    
    