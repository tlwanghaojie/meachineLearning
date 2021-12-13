# _*_ coding： utf-8 _*_ 
# @Time: 2021/12/10 20:08 
# @Author: WangHaojie 
# @File: fpGrowthTest 
# @Project: 机器学习实战
import fpGrowth
if __name__ == '__main__':
    # 构建FP树
    simpDat = fpGrowth.loadSimpDat()
    initSet = fpGrowth.createInitSet(simpDat)
    myFPtree, myHeaderTab = fpGrowth.createTree(initSet, 3)
    # myFPtree.disp()
    # 从一棵FP树中挖掘频繁项集
    fpGrowth.findPrefixPath('r', myHeaderTab['r'][1])
    freqItems = []
    fpGrowth.mineTree(myFPtree, myHeaderTab, 3, set([]), freqItems)
    print(freqItems)
