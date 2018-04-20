# -*- coding:utf-8 -*-

# get the deg_ac and degname
import re
def geneac_genename(filein):
    NClist = {}
    filein = open(filein, "r")
    #setlist = []
    #deglist = []
    for line in filein.readlines():
        if re.match("^#", line):
            #print(line)
            continue
        line = line.strip().split("	")
        if line[0] not in NClist.keys():
            setlist = set()
            setlist.add(line[1])
            NClist[line[0]]=setlist
        else:
            NClist[line[0]].add(line[1])
    return NClist
def genename_geneac(filein):
    NClist = {}
    filein = open(filein, "r")
    # setlist = []
    # deglist = []
    for line in filein.readlines():
        if re.match("^#", line):
            # print(line)
            continue
        line = line.strip().split("	")
        NClist[line[1]] = line[0]
    return NClist
#import sys
#import os
if __name__ == "__main__":
    #filepath = sys.argv[0]
    #NClist = geneac_genename("D://zola_workspace//worklab//entropyproject//essentialgene_dataset//deg-p-15.2//degannotation-p.dat")
    NClist = genename_geneac("D://zola_workspace//worklab//entropyproject//essentialgene_dataset//deg-p-15.2//degannotation-p.dat")
    print NClist
