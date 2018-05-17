# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

#梯度下降法的目标是通过合理的方法更新假设函数 hθ 的参数 θ 使得损失函数 J(θ) 对于所有样本最小化。
# 这个合理的方法的步骤如下:
#
# 根据经验设计假设函数和损失函数，以及假设函数所有 θ 的初始值
# 对损失函数求所有 θ 的偏导（梯度）: ∂J(θ)/∂θj
# 使用样本数据更新假设函数的 θ，更新公式为: θj=θj−α⋅∂J/∂θj (其中 α 为更新步长（调整参数的灵敏度，灵敏度太高容易振荡，灵敏度过低收敛缓慢）

import numpy as np
import matplotlib.pyplot as plt

def GD1():
    spaces = [45, 73, 89, 120, 140, 163]
    prices = [80, 150, 198, 230, 280, 360]
    spaces, prices = np.array(spaces), np.array(prices)  # numpy.array:使用列表生成一维数组

    # #-------画出房屋面积与房屋价格的散点图
    # plt.scatter(spaces,prices,c="g")
    # plt.xlabel("house space")
    # plt.ylabel("house price")
    # plt.show()

    # 设置theta的初始值
    theta0 = 0
    theta1 = 0

    # 选择步长alpha：如果步长选择不对，则theta参数更新结果可能会不对
    alpha = 0.00005
    # 当α过大时，有可能越过最小值，而α当过小时，容易造成迭代次数较多，收敛速度较慢。

    x_i0 = np.ones(len(spaces))  # 返回一个用1 填充的数组，一个参数表示这行的元素个数np.ones(5)：一行5列。np.ones((2, 1))：两行一列，都是1

    # 所以是返回一个有6个元素的一组数组
    # 假设函数h(x):
    def h(x):
        return theta0 + theta1 * x  # 一个x为一个特征

    # 损失函数
    def calc_error():
        return np.sum(np.power((h(spaces) - prices), 2)) / 2

    # 损失函数偏导数 （theta 0 和theta 1）
    def calc_delta0():
        return alpha * np.sum(h(spaces) - prices) * x_i0

    def calc_delta1():
        return alpha * np.sum(h(spaces) - prices) * spaces

    # 循环更新 theta 值并计算误差，停止条件为：
    #  1.误差小于某个值
    #  2.循环次数控制
    k = 0
    while True:
        delta0 = calc_delta0()
        delta1 = calc_delta1()
        theta0 = theta0 - delta0
        theta1 = theta1 - delta1
        error = calc_error()
        # print("delta [%f,%f],theta [%f,%f], error %f" % (delta0,delta1,theta0,theta1,error))
        print()

        k = k + 1
        if (k > 10 or error < 200):
            break
    # print("h(x)=%f + %f * x"%(theta0,theta1))

    # print('h(x)={}+{}*x'.format(theta0, theta1))
    # 使用假设函数计算出来的价格，用于画拟合曲线
    y_out = h(spaces)

    plt.scatter(spaces, prices, c="g")  # 绿色点表示房屋面积和价格数据的散点图
    plt.plot(spaces, y_out, c="b")  # 蓝色点表示使用梯度下降法拟合出来的曲线
    plt.xlabel("house space")
    plt.ylabel("house price")
    plt.show()
# GD1()


def GD2():
    # Training data set
    # each element in x represents (x1)
    x = [1, 2, 3, 4, 5, 6]
    # y[i] is the output of y =theta0 + theta1*x[1]
    y = [13, 14, 20, 21, 25, 30]
    # 设置允许误差值
    epsilon = 1
    # 学习率
    alpha = 0.01

    diff = [0, 0]
    max_itor = 20

    error0 = 0
    error1 = 0

    count = 1
    m = len(x)

    # init the parameters to zero
    theta0 = 0
    theta1 = 0
    error_list = []
    while 1:

        count = count + 1
        diff = [0, 0]
        for i in range(m):
            diff[0] += theta0 + theta1 * x[i] - y[i]
            diff[1] += (theta0 + theta1 * x[i] - y[i]) * x[i]
        theta0 = theta0 - alpha / m * diff[0]
        theta1 = theta0 - alpha / m * diff[1]
        error1 = 0

        for i in range(m):
            error1 += (theta0 + theta1 * x[i] - y[i]) ** 2
        error_list.append(error1)
        if abs(error1 - error0) < epsilon:
            break

        print("iterator :%d theta0 :%f,theta1 :%f,error:%f" % (count-1,theta0, theta1, error1))
        if count > 100:
            print("count>100...")
            break
    print("theta0 :%f,theta1 :%f,error:%f" % (theta0, theta1, error1))
    print("error_list为：",error_list)
    #-----画收敛图--
    # plt.scatter(x,y,c="g")
    n=len(error_list)
    ite=range(n)
    plt.plot(ite,error_list,c="r",linewidth=3)
    plt.title("Convergence curve")
    plt.xlabel("iteration")
    plt.ylabel("error")
    plt.show()

GD2()