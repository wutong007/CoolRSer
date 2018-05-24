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
    Prob =np.zeros(K) # 对应Prob数组：落在原类型的概率
    Alias =np.zeros(K,dtype=np.int) # 对应Alias数组：每一列第二层的类型

    #Sort the data into the outcomes with probabilities
    #that are larger and smaller than 1/K
    smaller =[] # 存储比1小的列
    larger =[] # 存储比1大的列

    for kk,prob in enumerate(probs):
        Prob[kk] =K*prob # 概率
        if Prob[kk] <1.0:
            smaller.append(kk)
        else:
            larger.append(kk)

    # Loop though and create little binary mixtures that appropriately allocate
    # the larger outcomes over the overall uniform mixture.

    #通过拼凑，将各个类别都凑为1
    while len(smaller) > 0 and len(larger) > 0:
        small =smaller.pop()
        large =larger.pop()

        Alias[small] =large #填充Alias数组
        Prob[large] =Prob[large]-(1.0 - Prob[small]) #将大的分到小的上

        if Prob[large] <1.0:
            smaller.append(large)
        else:
            larger.append(large)
    return Alias,Prob

def alias_draw(Alias,Prob):
    '''

    :param J: Alias数组
    :param q: Prob数组
    :return:一次采样结果
    '''
    K=len(Alias)

    # Draw from the overall uniform mixture.
    kk = int(np.floor(npr.rand()*K)) #随机取一列

    # Draw from the binary mixture, either keeping the small one, or choosing the associated larger one.
    # 采样过程：随机取某一列k（即[1,4]的随机整数，再随机产生一个[0-1]的小数c，）
    # 如果Prob[kk]大于c，
    if npr.rand() <Prob[kk]: #比较
        return kk
    else:
        return Alias[kk]

K=5
N=100

# Get a random probability vector.
probs =npr.dirichlet(np.ones(K),1).ravel() # .ravel(): 将多维数组降为一维

# Construct the table
Alias,Prob = alias_setup(probs)
print("Prob is :",Prob)
print("Alias is :",Alias)
# Prob is : [ 0.25058826  0.69258202  0.83010441  0.87901003  1.        ]
# Alias is : [4 4 4 4 0]


# Generate variates.
X = np.zeros(N)
for nn in range(N):
    X[nn] = alias_draw(Alias,Prob)