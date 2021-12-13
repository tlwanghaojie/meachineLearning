# _*_ coding： utf-8 _*_ 
# @Time: 2021/12/6 17:05 
# @Author: WangHaojie 
# @File: treesTest 二叉树
# @Project: 机器学习实战
import trees
if __name__ == '__main__':
    myDat, labels = trees.createDataSet()
    # ID3分类
    # myTree = trees.createTree(myDat, labels)

    myTree = trees.retrieveTree(0)
    # 决策树分类
    print(trees.classify(myTree, labels, [1, 0]))
