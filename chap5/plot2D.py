# _*_ coding： utf-8 _*_ 
# @Time: 2021/12/7 16:05 
# @Author: WangHaojie 
# @File: plot2D  分类绘制
# @Project: 机器学习实战
from numpy import *
import matplotlib.pyplot as plt
import logRegres
if __name__ == '__main__':
    dataMat, labelMat = logRegres.loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0]
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []

    markers = []
    colors = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1])
            ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    type1 = ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    type2 = ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    weights = [13.03822793, 1.32877317, -1.96702074]
    y = (-weights[0] - weights[1] * x) / weights[2]
    # plot返回对象需要解构
    type3, = ax.plot(x, y)
    ax.legend([type1, type2, type3], ["Did Not Like", "Liked in Small Doses", "Liked in Large Doses"], loc=2)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()
