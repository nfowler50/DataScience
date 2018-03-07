#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 20:57:06 2017

@author: nickfowler
"""
import sys, re, os
import csv
from collections import Counter
import math, random
import matplotlib.pyplot as plt
import numpy as np
import proba
from mpl_toolkits.mplot3d import axes3d
import linalgbera as la

#Input = input("TYPE: ")

print(os.getcwd())
os.chdir(r'/Users/nickfowler/DatA')
print(os.getcwd())
print(os.listdir())
with open("tab_delimited_stock_prices.txt",'r') as fi:
    #fi.write(Input + "\n\n\n")
    fi.seek(0,0)
    f=fi.read()
   # print(f)
    
#print(f)

with open('tab_delimited_stock_prices.txt', 'r') as f:
    reader=csv.reader(f, delimiter='\t')
    for row in reader:
        date=row[0]
        symbol=row[1]
        closing_price=float(row[2])
        process=(date,symbol,closing_price)
        print(process)
    
with open('colon_delimited_stock_prices.txt', 'r') as f:
    reader=csv.DictReader(f, delimiter=':')
    for row in reader:
        date=row["date"]
        symbol=row["symbol"]
        closing_price=float(row["closing_price"])
        process=(date,symbol,closing_price)
        print(process)
        #print(date,symbol,closing_price)

starts_with_hash=0

with open("SomeFile.txt",'r') as f:
    for line in f:
        if re.match("^#",line):
                    starts_with_hash+=1
                    
print (starts_with_hash)

def get_domain(email_address):
    return email_address.lower().split("@")[-1]

with open('email_addresses.txt','r') as f:
    domain_counts=Counter(get_domain(line.strip())
                          for line in f
                          if "@" in line)
    
print(domain_counts)
                              
                    





