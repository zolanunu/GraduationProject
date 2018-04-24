# -*- coding:utf-8 -*-

import os

import entropy as en
import mi
import cmi as cm
import kld
import numpy as np
import markov
import gtec
import tpec

# 传入的geneNameFile: DEG100**.txt, geneNameDir：每个genename对应有一条序列，一对一的，存瑞的路径名
def combineFeature(geneNameFileDir, geneNameFile, geneNameDir, label):
    fr = open(geneNameFileDir, "r")
    featureList = []
    for eachline in fr.readlines():
        featureItem = [label]
        geneName = eachline.strip()
        fr2 = open(geneNameDir + "/" + geneName, "r")
        geneFastaContent = fr2.readlines()
        if (len(geneFastaContent) < 2):
            print "geneFasta error, geneName %s: " %geneName
            continue
        seq = geneFastaContent[1]

        # 1.entropy 4d
        entropyValues, entropyDict  = en.entropy(seq)
        featureItem.extend(entropyValues)
        #print "geneName %s, length of current feature: %d, entropy: %s" %(geneName, len(featureItem), entropyValues )

        # 2.mi 17d
        miValues = mi.computeMI(seq)
        #print "geneName %s, length of current feature: %d, miValues: %s" % (geneName, len(featureItem), miValues)
        featureItem.extend(miValues)

        # 3.cmi 65d
        cmiValues = cm.cmi(seq)
        featureItem.extend(cmiValues)
        #print "geneName %s, length of current feature: %d, cmiValues: %s" % (geneName, len(featureItem), cmiValues)

        # 4.kld 3d
        kldValues = kld.computeKLValue(seq)
        featureItem.extend(kldValues)
        #print "geneName %s, length of current feature: %d, kldValues: %s" % (geneName, len(featureItem), kldValues)

        # 5.markov 2d
        markovValues = markov.getMarkovScore(seq, m=2)
        featureItem.extend(markovValues)
        #print "geneName %s, length of current feature: %d, markovValues: %s" % (geneName, len(featureItem), markovValues)

        # 广义拓扑熵 k=3,4,5 3d
        gtecvalues = []
        gtec3 = gtec.gtec(seq)
        gtecvalues.extend(gtec3)
        gtec4 = gtec.gtec(seq, 4)
        gtecvalues.extend(gtec4)
        gtec5 = gtec.gtec(seq, 5)
        gtecvalues.extend(gtec5)
        featureItem.extend(gtecvalues)
        #print "geneName %s, length of current feature: %d, gtec values: %s" % (geneName, len(featureItem), gtecvalues)

        # 拓扑熵 k=2,3,4,5 4d
        tpecvalues = []
        tpec3 = tpec.tpec(seq, 3)
        tpecvalues.extend(tpec3)
        tpec4 = tpec.tpec(seq, 4)
        tpecvalues.extend(tpec4)
        tpec5 = tpec.tpec(seq, 5)
        tpecvalues.extend(tpec5)
        featureItem.extend(tpecvalues)
        featureList.append(featureItem)
        #print "geneName %s, length of current feature: %d, tpec values: %s" % (geneName, len(featureItem), tpecvalues)
        featurefile = geneNameFile[:-4]+"_feature.data"
    np.savetxt(featurefile, featureList, fmt = '%.6f')

def features(ac_name_fileDir, geneNameDir, label = 1):
    # 遍历ac_name_fileDir 文件中的每一个txt文件
    rootDir = ac_name_fileDir
    list = os.listdir(rootDir)
    print(len(list))
    for i in range(0, len(list)):
        path = os.path.join(rootDir, list[i])
        combineFeature(path, list[i], geneNameDir, label)
    print("done")
if __name__ == "__main__":
    #print("DEG1001.txt"[:-4])
    features("ac_name_np", "degone-15.2-np", -1)
    #geneNameFile = "train_gene.data"
    #geneNameDir = "degone-15.2-p"
    #features = combineFeature(geneNameFile, geneNameDir)
    #np.savetxt("train.data", features, fmt='%.6f', delimiter='\t')

