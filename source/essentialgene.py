# -*- coding:utf-8 -*-

import geneac_name
import geneac_organism
import re
import os
import splitFasta

def get_key(dict, value):
    return [k for k, v in dict.items() if v == value]

#将AC的geneName放到一起
def changeFram(acAndGeneName={}):
    values = list(set(acAndGeneName.values())) #获取所有的AC
    geneNames = acAndGeneName.keys()

    acDict = {}
    for acItem in values:
        subGeneName = []
        for geneNameItem in geneNames:
            acNow = acAndGeneName.get(geneNameItem) #获取当前gene所属的ac
            if acNow == acItem:
                subGeneName.append(geneNameItem)
        acDict[acItem] = subGeneName
    return acDict

def combileByAcName(acDict, inputDir, outdir):
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    keys = acDict.keys()
    for acName in keys:
        values = acDict[acName]
        subFasta = ""
        for geneName in values:
            fr = open(inputDir + "/" + geneName, "r")
            content = fr.readlines()
            subFasta += "".join(content) + "\n"
            fr.close()
        fw = open(outdir + "/" + acName + ".fasta", "w")
        fw.write(subFasta)
        fw.close()

if __name__ == "__main__":
    #NCOlist = geneac_organism.geneac_organism("D://zola_workspace//worklab//entropyproject//essentialgene_dataset//deg-p-15.2//degannotation-p.dat")
    NClist = geneac_name.genename_geneac("D://zola_workspace//worklab//entropyproject//essentialgene_dataset//deg-np-15.2//degannotation-np.dat")

    acDict = changeFram(NClist)
    print(len(acDict.keys()))
    #print(acDict)
    #print acDict
    deg_one_np = "degone-15.2-np"
    splitFasta.splitFasta("D://zola_workspace//worklab//entropyproject//essentialgene_dataset//deg-np-15.2//degseq-np.dat", deg_one_np)
    deg_multi_np = "degm-15.2-np"
    combileByAcName(acDict, deg_one_np, deg_multi_np)