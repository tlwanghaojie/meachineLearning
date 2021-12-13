# _*_ coding： utf-8 _*_ 
# @Time: 2021/12/8 16:07 
# @Author: WangHaojie 
# @File: adaboostTest 元算法
# @Project: 机器学习实战
import adaboost
from numpy import *
if __name__ == '__main__':
    # 在一个简单的数据集上使用adaboost
    # datArr, labelArr = adaboost.loadSimpData()
    # # D = mat(ones((5, 1)) / 5)
    # print(adaboost.buildStump(datMat, classLabels, D))
    # classifierArray = adaboost.adaBoostTrainDS(datArr, labelArr, 30)
    # adaboost.adaClassify([0, 0], classifierArray)

    # 在一个难数据集上使用adaboost--预测患有疝病的马是否能够存活
    dataArr, labelArr = adaboost.loadDataSet('horseColicTraining2.txt')
    classifierArray, aggClassEst = adaboost.adaBoostTrainDS(dataArr, labelArr, 10)
    testArr, testLabelArr = adaboost.loadDataSet('horseColicTest2.txt')
    prediction10 = adaboost.adaClassify(testArr, classifierArray)
    errArr = mat(ones((67, 1)))
    print(errArr[prediction10 != mat(testLabelArr).T].sum())
    adaboost.plotROC(aggClassEst.T, labelArr)
