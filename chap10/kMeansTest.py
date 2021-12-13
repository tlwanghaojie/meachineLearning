# _*_ coding： utf-8 _*_ 
# @Time: 2021/12/9 16:21 
# @Author: WangHaojie 
# @File: kMeansTest K均值算法
# @Project: 机器学习实战
import kMeans
from numpy import *
if __name__ == '__main__':
    # datMat = mat(kMeans.loadDataSet('testSet.txt'))
    # myCentroids, clustAssing = kMeans.kMeans(datMat, 4)

    # 二分k均值聚类算法
    # datMat3 = mat(kMeans.loadDataSet('testSet2.txt'))
    # centList, myNewAssments = kMeans.biKmeans(datMat3, 3)
    # print(centList)  # 质心

    # 对地图上的点进行聚类
    kMeans.clusterClubs(5)
