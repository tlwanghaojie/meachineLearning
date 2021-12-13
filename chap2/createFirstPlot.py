# _*_ coding： utf-8 _*_ 
# @Time: 2021/12/6 16:22 
# @Author: WangHaojie 
# @File: createFirstPlot 
# @Project: 机器学习实战

from numpy import *
import KNN
import matplotlib.pyplot as plt

if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111)
    datingDataMat, datingLabels = KNN.file2matrix('datingTestSet2.txt')
    ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0 * array(datingLabels), 15.0 * array(datingLabels))
    ax.axis([-2, 25, -0.2, 2.0])
    plt.xlabel('Percentage of Time Spent Playing Video Games')
    plt.ylabel('Liters of Ice Cream Consumed Per Week')
    plt.show()
