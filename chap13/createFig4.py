# _*_ coding： utf-8 _*_ 
# @Time: 2021/12/10 10:46 
# @Author: WangHaojie 
# @File: createFig4 
# @Project: 机器学习实战
from numpy import *
import matplotlib.pyplot as plt
import pca
if __name__ == '__main__':
    dataMat = pca.replaceNanWithMean()
    meanVals = mean(dataMat, axis=0)
    meanRemoved = dataMat - meanVals  # remove mean
    covMat = cov(meanRemoved, rowvar=0)
    eigVals, eigVects = linalg.eig(mat(covMat))
    eigValInd = argsort(eigVals)  # sort, sort goes smallest to largest
    eigValInd = eigValInd[::-1]  # reverse
    sortedEigVals = eigVals[eigValInd]
    total = sum(sortedEigVals)
    varPercentage = sortedEigVals / total * 100
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(range(1, 21), varPercentage[:20], marker='^')
    plt.xlabel('Principal Component Number')
    plt.ylabel('Percentage of Variance')
    plt.show()
