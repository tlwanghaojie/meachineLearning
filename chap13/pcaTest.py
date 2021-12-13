# _*_ coding： utf-8 _*_ 
# @Time: 2021/12/10 11:03 
# @Author: WangHaojie 
# @File: pcaTest 
# @Project: 机器学习实战
import pca
from numpy import *
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
if __name__ == '__main__':
    iris = load_iris()
    x_data = iris.data
    y_data = iris.target
    lowDDataMat, reconMat = pca.pca(x_data, 2)
    x = array(lowDDataMat)[:, 0]
    y = array(lowDDataMat)[:, 1]
    plt.scatter(x, y, c=y_data)
    plt.show()
