# !/usr/bin/env python
# encoding: utf-8
__author__ = 'ScarlettZero'

# 20180522
# AliasMethod Sampling

import numpy as np
import pandas as pd
import numpy.random as npr

def alias_setup(probs):
    '''

    :param probs: 某个概率分布
    :return: Alias数组与Prob数组
    '''
    K =len(probs) # K为类别数目
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

def alias_draw(J,q):
    '''

    :param J: Alias数组
    :param q: Prob数组
    :return:一次采样结果
    '''
    K=len(J)

    # Draw from the overall uniform mixture.
    kk = int(np.floor(npr.rand()*K)) #随机取一列

    # Draw from the binary mixture, either keeping the small one, or choosing the associated larger one.
    if npr.rand() <q[kk]: #比较
        return kk
    else:
        return J[kk]

K=5
N=100

# Get a random probability vector.
probs =npr.dirichlet(np.ones(K),1).ravel() # .ravel(): 将多维数组降为一维

# Construct the table
J,q = alias_setup(probs)

# Generate variates.
X = np.zeros(N)
for nn in range(N):
    X[nn] = alias_draw(J,q)