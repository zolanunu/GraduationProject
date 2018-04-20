# -*- coding:utf-8 -*-

import extractgene
import geneac_organism
import re
import os
def essentialgene(filein, fileout_path, genenamedictl, geneacorganismdictl):
    if not os.path.exists(fileout_path):
        os.makedirs(fileout_path)
    filein = open(filein, "r")
    #key = genenamedictl.keys()
    prefix = "NC_009085"
    fw = open(prefix.strip()+"-p.txt", "a")
    #count = 0
    for line in filein.readlines():
        if (re.match("^>", line)):
            degac = genenamedictl[line.strip()[1:]]
            prefix = geneacorganismdictl[degac]
            fw.close()
            fw = open(fileout_path+"/"+prefix.strip()+"-p.txt", "a")
            fw.write(prefix+line)
        else:
            fw.write(line)
        print(line)
    fw.close()

if __name__ == "__main__":
    NCOlist = geneac_organism.geneac_organism("D://zola_workspace//worklab//entropyproject//essentialgene_dataset//deg-np-15.2//degannotation-np.dat")
    NClist = extractgene.genename_geneac("D://zola_workspace//worklab//entropyproject//essentialgene_dataset//deg-np-15.2//degannotation-np.dat")
    essentialgene("D://zola_workspace//worklab//entropyproject//essentialgene_dataset//deg-np-15.2//degseq-np.dat", "D://zola_workspace//worklab//entropyproject//essentialgene_dataset//deg-np-15.2", NClist,NCOlist)
