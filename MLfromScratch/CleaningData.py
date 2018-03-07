#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 22:00:20 2017

@author: nickfowler
"""
import math, proba, random, csv, dateutil.parser, datetime
from collections import Counter, defaultdict
import matplotlib.pyplot as plt
import numpy as np

   
def parse_rows_with(reader, parsers):
    for row in reader:
        yield parse_row(row, parsers)
        
def try_or_none(f):
    def f_or_none(x):
        try: return f(x)
        except: return None
    return f_or_none

def parse_row(input_rows, parsers):
    return[try_or_none(parser)(value) if parser is not None else value
           for value, parser in zip(input_rows, parsers)]
    
def try_parse_field(field_name, value, parser_dict):
    parser=parser_dict.get(field_name) #none if no such entry
    if parser is not None:
        return try_or_none(parser)(value)
    else:
        return value
    
def parse_dict(input_dict, parser_dict):
    return {field_name: try_parse_field(field_name, value, parser_dict)
            for field_name, value in input_dict.iteritems()}
    
data=[]

with open("comma_delimited_stock_prices.csv","r") as f:
    reader=csv.reader(f)
    for line in parse_rows_with(reader, [dateutil.parser.parse, None, float]):
        data.append(line)
        
for row in data:
    if any(x is None for x in row):
        print(row)
        
data=[
      {'closing_price': 102.61,
       'date':datetime.datetime(2014,8,29,0,0),
       'symbol':'AAPL'},
      {'closing_price': 93.61,
       'date':datetime.datetime(2014,8,30,0,0),
       'symbol':'AAPL'},
      {'closing_price': 105.61,
       'date':datetime.datetime(2014,8,29,0,0),
       'symbol':'MSFT'},
      {'closing_price': 104,
       'date':datetime.datetime(2014,8,26,0,0),
       'symbol':'AAPL'},
      {'closing_price': 91,
       'date':datetime.datetime(2014,8,24,0,0),
       'symbol':'AAPL'}]

max_aapl_price=max(row["closing_price"]
                   for row in data
                   if row['symbol']=='AAPL')

#print(max_aapl_price)
#print(list(data[2].values())[1])
#print(list(row["closing_price"] for row in data if 'symbol'=='AAPL'))

def picker(field_name):
    return lambda row: row[field_name]

def pluck(field_name, rows):
    """turn a list of dicts into a list of field name values"""
    return map(picker(field_name), rows)

def group_by(grouper, rows, value_transform=None):
    #key is output of grouper, value is list of rows
    grouped=defaultdict(list)
    for row in rows:
        grouped[grouper(row)].append(row)
        
    if value_transform is None:
        return grouped
    else:
        return {key: value_transform(row)
                for key, row in grouped.items()}

max_price_by_sym=group_by(picker('symbol'),
                          data,
                          lambda rows: max(pluck("closing_price", rows)))


#print(picker('symbol')(data[2]))
print(max_price_by_sym)






