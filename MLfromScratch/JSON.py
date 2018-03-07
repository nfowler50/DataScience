#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 18:46:58 2017

@author: nickfowler
"""

import json, requests
from dateutil.parser import parse
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

serialized="""{"title": "Data Science Book",
            "author": "Joel Grus",
            "publication": 2014,
            "topics": ["python","data","science","data science"]}"""

deserialized=json.loads(serialized)
if "data science" in deserialized["topics"]:
    print(deserialized)
    
#unauthenticated API
    
endpoint="https://api.github.com/users/joelgrus/repos"

repos=json.loads(requests.get(endpoint).text)
#print(repos[1])

dates=[parse(repo["created_at"]) for repo in repos]
month_counts=Counter(date.month for date in dates)
weekday_counts=Counter(date.weekday() for date in dates)

last_5_repos=sorted(repos,
                    key=lambda r: r["created_at"],
                    reverse=True)[:5]

last_5_langs=[repo["language"]
              for repo in last_5_repos]

timec=Counter(date.time().hour for date in dates)

#print(dates[1].time().hour)
#print(timec)
'''
plt.bar(range(len(timec)), timec.values(), align='center')
plt.xticks(range(len(timec)), timec.keys())
'''
print(timec)
#print(timec[17])


times=sorted(timec.keys())
timecount=[timec.get(x)` for x in times]

#print(timecount)
#times=sorted(timec, timec.get())
#print(timecount,'\n',times)

plt.bar(times, timecount)
plt.xticks(range(0,24,2))

