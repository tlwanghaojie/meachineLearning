# _*_ coding： utf-8 _*_ 
# @Time: 2021/12/9 17:42 
# @Author: WangHaojie 
# @File: aprioriTest  Apriori算法
# @Project: 机器学习实战
import apriori
if __name__ == '__main__':
    # dataSet = apriori.loadDataSet()
    # C1 = apriori.createC1(dataSet)
    # D = list(map(set, dataSet))
    # L1, suppDataO = apriori.scanD(D, C1, 0.5)
    # print(L1)

    # 使用apriori算法
    # dataSet = apriori.loadDataSet()
    # # 尝试一下70%的支持度
    # L, suppData = apriori.apriori(dataSet, minSupport=0.7)
    # print(L)

    # 从频繁项集中挖掘关联规则
    # dataSet = apriori.loadDataSet()
    # L, suppData = apriori.apriori(dataSet, minSupport=0.5)
    # rules = apriori.generateRules(L, suppData, minConf=0.5)
    # print(rules)

    # 发现毒蘑菇的相似特征
    mushDatSet = [line.split() for line in open('mushroom.dat').readlines()]
    L, suppData = apriori.apriori(mushDatSet, minSupport=0.3)
    for item in L[1]:
        if item.intersection('2'):
            print(item)
