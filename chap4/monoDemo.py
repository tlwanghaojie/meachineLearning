# _*_ coding： utf-8 _*_ 
# @Time: 2021/12/7 10:27 
# @Author: WangHaojie 
# @File: monoDemo 函数绘制
# @Project: 机器学习实战
from numpy import *
import matplotlib.pyplot as plt

if __name__ == '__main__':
    t = arange(0.01, 0.5, 0.01)
    s = sin(2*pi*t)
    logS = log(s)
    fig = plt.figure()

    ax = fig.add_subplot(211)
    ax.plot(t, s)
    ax.set_ylabel('f(x)')
    ax.set_xlabel('x')

    ax = fig.add_subplot(212)
    ax.plot(t, logS)
    ax.set_ylabel('ln(f(x))')
    ax.set_xlabel('x')
    plt.show()
