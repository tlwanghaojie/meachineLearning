# _*_ coding： utf-8 _*_ 
# @Time: 2021/12/9 14:51 
# @Author: WangHaojie 
# @File: regTreesTest  回归树
# @Project: 机器学习实战
import regTrees
from numpy import *
import matplotlib.pyplot as plt
import matplotlib
if __name__ == '__main__':
    # 数据切分
    # testMat = mat(eye(4))
    # mat0, mat1 = regTrees.binSplitDataSet(testMat, 1, 0.5)
    # print(mat0)
    # print(mat1)

    # 将CART算法用于回归
    # myDat = regTrees.loadDataSet('ex00.txt')
    # myMat = mat(myDat)
    # print(regTrees.createTree(myMat))
    # myDat1 = regTrees.loadDataSet('ex0.txt')
    # myMat1 = mat(myDat1)
    # print(regTrees.createTree(myMat1))

    # # 预剪枝
    # myDat2 = regTrees.loadDataSet('ex2.txt')
    # myMat2 = mat(myDat2)
    # print(regTrees.createTree(myMat2))
    # print(regTrees.createTree(myMat2, ops=(10000, 4)))
    # # 后剪枝
    # myTree = regTrees.createTree(myMat2, ops=(0, 1))
    # myDatTest = regTrees.loadDataSet('ex2test.txt')
    # myMat2Test = mat(myDatTest)
    # print(regTrees.prune(myTree, myMat2Test))

    # 模型树
    # myMat2 = mat(regTrees.loadDataSet('exp2.txt'))
    # print(regTrees.createTree(myMat2, regTrees.modelLeaf, regTrees.modelErr, (1, 10)))

    # 1.绘图
    trainMat = mat(regTrees.loadDataSet('bikeSpeedVsIq_train.txt'))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(trainMat[:, 0].T.flatten().A[0], trainMat[:, 1].T.flatten().A[0])
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False
    plt.xlabel('骑自行车的速度')
    plt.ylabel('智商IQ')
    plt.show()
    # 2.树回归与标准回归的比较
    trainMat = mat(regTrees.loadDataSet('bikeSpeedVsIq_train.txt'))
    testMat = mat(regTrees.loadDataSet('bikeSpeedVsIq_test.txt'))
    myTree = regTrees.createTree(trainMat, ops=(1, 20))
    yHat = regTrees.createForeCast(myTree, testMat[:, 0])
    print(corrcoef(yHat, testMat[:, 1], rowvar=0)[0, 1])
    ws, X, Y = regTrees.linearSolve(trainMat)
    for i in range(shape(testMat)[0]):
        yHat[i] = testMat[i, 0] * ws[1, 0] + ws[0, 0]
    print(corrcoef(yHat, testMat[:, 1], rowvar=0)[0, 1])
