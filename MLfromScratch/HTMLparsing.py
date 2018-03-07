#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 18:28:56 2017

@author: nickfowler
"""

import sys, re, os, csv, math, random, proba, requests
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import linalgbera as la
from bs4 import BeautifulSoup as BS
from string import digits

'''
html=requests.get("https://en.wikipedia.org/wiki/Science").text
soup=BS(html,'html5lib')

first_p=soup.find('p')   #or just soup.p

first_p_text=soup.find('p').text
first_p_words=soup.p.text.split()

first_p_id=soup.p.get('id')

all_paragraphs=soup.find_all('p')   #or just soup('p')
p_with_id=[p for p in soup('p') if p.get('id')]

important_p=soup('p', {'class' : 'important'})
important_p2=soup('p','important')
important_p3=[p for p in soup('p')
              if 'important' in p.get('class',[])]

'''

url="http://www.learndatasci.com/free-data-science-books/"
soup=BS(requests.get(url).text,'html5lib')

titles=soup('h3','w-hidden-main w-hidden-medium title-phone')
tds=soup('div', 'w-row item')


print(len(titles))
print(len(tds))
reviewlink=tds[4]('a','w-button amazon btn btn-2 icon-arrow-right btn-3e')
#print(tds.text)


def has_review(td):
    reviewlink=td('a',"w-button amazon btn btn-2 icon-arrow-right btn-3e")
    return (len(reviewlink)==1) # and reviewlink[0].textstrip().startswith('See'))

#x=h3 for h3 in titles if has_review(h3)

#print(len[td for td in tds])
review_links=[has_review(td) for td in tds if has_review(td)]
print(len(review_links))


author=tds[3].find('h4','author').text.split('by ')[1]
#authorsplit=re.findall('\D+',author)
#authorclean=re.split('[,&]+', authorsplit[0])
authorclean=re.split('[,&]+', re.findall('\D+',author)[0])
authorclean2=authorclean[0:(len(authorclean)-1)]
#authorclean=authorsplit[0].split('&')
#authorsplits=authorsplit[0].split('by ')[1].split(',')
year=re.findall('\d+', author)[0]

tit=soup('div','w-col w-col-3 w-col-small-6 w-col-tiny-6 w-clearfix')
print(tit[3].text)



#.split('by ')[1].split(', ')


#altname=tds[3].find('img','cover')
#print(year, authorclean2)

def book_info(td):
    #pull info and return a dict
    title=td.find('h3','w-hidden-small w-hidden-tiny title phone').text
    authord=td.find('h4','author').text.split('by ')[1]
    authorclean=re.split('[,&]+', re.findall('\D+',authord)[0])
    author=authorclean[0:(len(authorclean)-1)]
    year=re.findall('\d+', authord)[0]
    return {'title':title, 'authors':author, 'year':year}
    #print(title, author, year)
    
print(book_info(tds[3]))

#all_books=[book_info(tds[i]) for i in range(100)]
#all_books=[book_info(td) for td in tds] 

#print(all_books)

