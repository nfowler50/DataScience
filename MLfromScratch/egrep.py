#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 20:38:13 2017

@author: nickfowler
"""

import sys, re

regex=sys.argv[1]

for line in sys.stdin:
    if re.search(regex,line):
        sys.stdout.write(line)
