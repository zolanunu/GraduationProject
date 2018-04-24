# -*- coding:utf-8 -*-
import re
def geneac_organism(filein):
    fout= open("genename_organism-np.txt", "w")
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
        fout.write(line[0]+" "+line[8]+"\n")
    fout.close()
    return NClist

if __name__ == "__main__":
    NClist = geneac_organism("D://zola_workspace//worklab//entropyproject//essentialgene_dataset//deg-np-15.2//degannotation-np.dat")
    print NClist
