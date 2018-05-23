# !/usr/bin/env python
# encoding: utf-8
__author__ = 'ScarlettZero'

# 20180522
# AliasMethod Sampling

import numpy as np
import pandas as pd

def alias_setup(probs):
    '''

    :param probs: 某个概率分布
    :return: Alias数组与Prob数组
    '''
    K =len(probs)
    q =np.zeros(K) #对应Prob数组
    J =np.zeros(K,dtype=np.int) #对应Alias数组

    #Sort the data into the outcomes with probabilities
    #that are larger and smaller than 1/K
    smaller =[] #存储比1小的列
    larger =[] #存储比1大的列

    for kk,prob in enumerate(probs):
        


