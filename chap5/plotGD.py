# _*_ coding： utf-8 _*_ 
# @Time: 2021/12/7 16:48 
# @Author: WangHaojie 
# @File: plotGD 梯度下降绘制
# @Project: 机器学习实战
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

from chap3.treePlotter import arrow_args

if __name__ == '__main__':
    leafNode = dict(boxstyle='round4', fc="0.8")
    matplotlib.rcParams['xtick.direction'] = 'out'
    matplotlib.rcParams['ytick.direction'] = 'out'
    delta = 0.025
    x = np.arange(-2.0, 2.0, delta)
    y = np.arange(-2.0, 2.0, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = -((X - 1) ** 2)
    Z2 = -(Y ** 2)
    Z = 1.0 * (Z2 + Z1) + 5.0
    plt.figure()
    CS = plt.contour(X, Y, Z)
    plt.annotate('', xy=(0.05, 0.05), xycoords='axes fraction',
                 xytext=(0.2, 0.2), textcoords='axes fraction',
                 va="center", ha="center", bbox=leafNode, arrowprops=arrow_args)
    plt.text(-1.9, -1.8, 'P0')
    plt.annotate('', xy=(0.2, 0.2), xycoords='axes fraction',
                 xytext=(0.35, 0.3), textcoords='axes fraction',
                 va="center", ha="center", bbox=leafNode, arrowprops=arrow_args)
    plt.text(-1.35, -1.23, 'P1')
    plt.annotate('', xy=(0.35, 0.3), xycoords='axes fraction',
                 xytext=(0.45, 0.35), textcoords='axes fraction',
                 va="center", ha="center", bbox=leafNode, arrowprops=arrow_args)
    plt.text(-0.7, -0.8, 'P2')
    plt.text(-0.3, -0.6, 'P3')
    plt.clabel(CS, inline=1, fontsize=10)
    plt.title('Gradient Ascent')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
