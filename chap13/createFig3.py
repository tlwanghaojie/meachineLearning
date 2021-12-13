# _*_ coding： utf-8 _*_ 
# @Time: 2021/12/10 10:27 
# @Author: WangHaojie 
# @File: createFig3 
# @Project: 机器学习实战
from numpy import *
import matplotlib.pyplot as plt
import pca

if __name__ == '__main__':
    xcord0 = []
    ycord0 = []
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    markers = []
    colors = []
    myDat = pca.loadDataSet('testSet3.txt')
    for i in range(len(myDat)):
        if myDat[:, 2][i] == 0:
            xcord0.append(myDat[:, 0][i])
            ycord0.append(myDat[:, 1][i])
        if myDat[:, 2][i] == 1:
            xcord1.append(myDat[:, 0][i])
            ycord1.append(myDat[:, 1][i])
        if myDat[:, 2][i] == 2:
            xcord2.append(myDat[:, 0][i])
            ycord2.append(myDat[:, 1][i])
    fig = plt.figure()
    ax = fig.add_subplot(211)
    ax.scatter(xcord0, ycord0, marker='^', s=90)
    ax.scatter(xcord1, ycord1, marker='o', s=50, c='red')
    ax.scatter(xcord2, ycord2, marker='v', s=50, c='yellow')
    ax = fig.add_subplot(212)
    lowDDat, reconDat = pca.pca(myDat[:, 0:2], 1)
    label0Mat = lowDDat[nonzero(myDat[:, 2] == 0)[0], :2][0]  # get the items with label 0
    label1Mat = lowDDat[nonzero(myDat[:, 2] == 1)[0], :2][0]  # get the items with label 1
    label2Mat = lowDDat[nonzero(myDat[:, 2] == 2)[0], :2][0]  # get the items with label 2
    ax.scatter(label0Mat[:, 0].flatten().A[0], zeros(shape(label0Mat)[0]), marker='^', s=90)
    ax.scatter(label1Mat[:, 0].flatten().A[0], zeros(shape(label1Mat)[0]), marker='o', s=50, c='red')
    ax.scatter(label2Mat[:, 0].flatten().A[0], zeros(shape(label2Mat)[0]), marker='v', s=50, c='yellow')
    plt.show()
