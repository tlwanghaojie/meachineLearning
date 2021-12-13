# _*_ coding： utf-8 _*_ 
# @Time: 2021/12/7 15:58 
# @Author: WangHaojie 
# @File: sigmoidPlot sigmoid函数
# @Project: 机器学习实战
from pylab import *
if __name__ == '__main__':
    t = arange(-60.0, 60.3, 0.1)
    s = 1 / (1 + exp(-t))
    ax = subplot(211)
    ax.plot(t, s)
    ax.axis([-5, 5, 0, 1])
    plt.xlabel('x')
    plt.ylabel('Sigmoid(x)')
    ax = subplot(212)
    ax.plot(t, s)
    ax.axis([-60, 60, 0, 1])
    plt.xlabel('x')
    plt.ylabel('Sigmoid(x)')
    show()
