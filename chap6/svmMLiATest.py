# _*_ coding： utf-8 _*_ 
# @Time: 2021/12/8 13:23 
# @Author: WangHaojie 
# @File: svmMLiATest  支持向量机
# @Project: 机器学习实战
import svmMLiA
from numpy import *
if __name__ == '__main__':
    dataArr, labelArr = svmMLiA.loadDataSet('testSet.txt')
    # b, alphas = svmMLiA.smoSimple(dataArr, labelArr, 0.6, 0.001, 40)
    b, alphas = svmMLiA.smoP(dataArr, labelArr, 0.6, 0.001, 40)
    ws = svmMLiA.calcWs(alphas, dataArr, labelArr)
    dataMat = svmMLiA.mat(dataArr)
    print(dataMat[0]*mat(ws) + b)
    svmMLiA.testRbf()
    svmMLiA.testDigits(('rbf', 10))
