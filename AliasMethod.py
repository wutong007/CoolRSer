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
        q[kk] =K*prob #概率
        if q[kk] <1.0:
            smaller.append(kk)
        else:
            larger.append(kk)

    # Loop though and create little binary mixtures that appropriately allocate
    # the larger outcomes over the overall uniform mixture.

    #通过拼凑，将各个类别都凑为1
    while len(smaller) >0 and len(larger) >0:
        small =smaller.pop()
        large =larger.pop()

        J[small] =large #填充Alias数组
        q[large] =q[large]-(1.0 - q[small]) #将大的分到小的上

        if q[large] <1.0:
            smaller.append(large)
        else:
            larger.append(large)
    return J,q



