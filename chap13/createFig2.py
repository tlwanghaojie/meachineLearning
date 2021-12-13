# _*_ coding： utf-8 _*_ 
# @Time: 2021/12/10 10:10 
# @Author: WangHaojie 
# @File: createFig2 
# @Project: 机器学习实战
import matplotlib.pyplot as plt
import pca

if __name__ == '__main__':
    dataMat = pca.loadDataSet('testSet.txt')
    lowDMat, reconMat = pca.pca(dataMat, 1)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(dataMat[:, 0].flatten().A[0], dataMat[:, 1].flatten().A[0], marker='^', s=90)
    ax.scatter(reconMat[:, 0].flatten().A[0], reconMat[:, 1].flatten().A[0], marker='o', s=50, c='red')
    plt.show()
