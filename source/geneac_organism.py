# -*- coding:utf-8 -*-
import re
def geneac_organism(filein):
    NClist = {}
    filein = open(filein, "r")
    # setlist = []
    # deglist = []
    for line in filein.readlines():
        if re.match("^#", line):
            # print(line)
            continue
        line = line.strip().split("	")
        NClist[line[0]] = line[8]
    return NClist

if __name__ == "__main__":
    NClist = geneac_organism("D://zola_workspace//worklab//entropyproject//essentialgene_dataset//deg-p-15.2//degannotation-p.dat")
    print NClist