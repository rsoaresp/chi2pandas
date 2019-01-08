#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 21:57:41 2019

@author: rsoares
"""

import numpy as np
import pandas as pd

from itertools import product


def chi2(df):

    n = (len(df.columns) - 1)*(len(df.index) - 1)    
    expected = df.copy()
    
    for i in product(df.index, df.columns):
        total = df.values.sum()
        expected.loc[i[0], i[1]] = df.loc[i[0], :].sum()*df.loc[:, i[1]].sum()/total
          
    chi2 = ((df - expected)**2).divide(expected).values.sum()
        
    return expected, chi2