# -*- coding:utf-8 -*-

from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn import svm
import pandas as pd

def loaddataSet(featurefile):
    numFeat =  len(open(featurefile).readline().split(" "))
    dataMat = []
    labelMat = []
    fr = open(featurefile)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split(" ")
        for i in range(1,numFeat - 1):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[0]))
    return dataMat, labelMat


if __name__=="__main__":
    #loaddataSet("features\\DEG1001_p_feature.data", "features\\DEG1001_np_feature.data")
    dataMat, labelMat = loaddataSet("D://zola_workspace//worklab//entropyproject//source//featrues//DEG1001_feature.data")
    clf = RandomForestClassifier(n_estimators=10, criterion='gini', max_depth=None,
    min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features='auto', max_leaf_nodes=None,
    bootstrap=True, oob_score=False, n_jobs=1, random_state=None, verbose=0, warm_start=False, class_weight=None)


    scores = cross_val_score(clf, dataMat, labelMat)

    print(scores.mean())
    print(len(dataMat), len(labelMat))