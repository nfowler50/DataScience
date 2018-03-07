#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:08:44 2017

@author: nickfowler
"""


from twython import Twython, TwythonStreamer
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

Con_key='XbDx5q4RresDBPu69Wk4vqgsq'
Con_sec='V4pAfNBT7zQRXKgzuIzKuzazPXzfC8v4mPezd92APudVJtnfHd'
Acc_tok='929048575459311616-kMrix1BeyFSxNfN9meMSuUyPR3JgFbX'
Acc_sec='VsM1RNzGHtSgd7VxDLflCVbb0SdG2g1NCR2NbDiC3Rnzr'

twitter=Twython(Con_key, Con_sec)
'''
for status in twitter.search(q='"data science"')["statuses"]:
    user=status["user"]["screen_name"].encode('utf-8')
    text=status["text"].encode('utf-8')
    #print (user, ":",text)
''' 
#let's try the streamer

#tweets=[]
class MyStreamer(TwythonStreamer):
    """our own subclass of twython's streamer class"""
    
    def on_success(self,data):
        #let's store tweets in a list of tuples
        if data['lang']=='en':
            tweets.append(data)
            print('received tweet #', len(tweets))
                  
        if len(tweets)>1000:
            self.disconnect()
            print('done')
            
    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()

#search=input("Which tweets would you like to pull data on? ")
stream=MyStreamer(Con_key,Con_sec,Acc_tok,Acc_sec)
stream.statuses.filter(track=search.lower())

top_hashtags=Counter(hashtag['text'].lower() 
             for tweet in tweets
             for hashtag in tweet["entities"]["hashtags"])

top=top_hashtags.most_common(10)
print(top)


topic, posts=zip(*top)
plt.bar(range(len(topic)), posts, align='center')
plt.xticks(np.arange(len(topic)), topic, rotation=45, ha='right')
plt.ylabel('# of posts')
plt.xlabel('hashtag used')





