# _*_ coding： utf-8 _*_ 
# @Time: 2021/12/8 17:08 
# @Author: WangHaojie 
# @File: regressionTest (线性回归、局部加权线性回归、岭回归和逐步线性回归)
# @Project: 机器学习实战
import regression
from numpy import *
import matplotlib.pyplot as plt
if __name__ == '__main__':
    # 标准回归
    # xArr, yArr = regression.loadDataSet('ex0.txt')
    # ws = regression.standRegres(xArr, yArr)
    # xMat = mat(xArr)
    # yMat = mat(yArr)
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.scatter(xMat[:, 1].flatten().A[0], yMat.T[:, 0].flatten().A[0])
    # xCopy = xMat.copy()
    # xCopy.sort(0)
    # yHat = xCopy * ws
    # ax.plot(xCopy[:, 1], yHat)
    # plt.show()

    # 局部加权线性回归
    # xArr, yArr = regression.loadDataSet('ex0.txt')
    # yHat = regression.lwlrTest(xArr, xArr, yArr, 0.03)
    # xMat = mat(xArr)
    # yMat = mat(yArr)
    # strInd = xMat[:, 1].argsort(0)
    # xSort = xMat[strInd][:, 0, :]
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.plot(xSort[:, 1], yHat[strInd])
    # ax.scatter(xMat[:, 1].flatten().A[0], yMat.T.flatten().A[0], s=2, c='red')
    # plt.show()

    # 岭回归
    # abX, abY = regression.loadDataSet('abalone.txt')
    # ridgeWeights = regression.ridgeTest(abX, abY)
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.plot(ridgeWeights)
    # plt.show()

    # 逐步向前回归
    abX, abY = regression.loadDataSet('abalone.txt')
    ridgeWeights = regression.stageWise(abX, abY, 0.005, 1000)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(ridgeWeights)
    plt.show()
