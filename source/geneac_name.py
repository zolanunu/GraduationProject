# -*- coding:utf-8 -*-

# gneac_genename: ac-name的字典对应，一对一，并写入一个文件中
# generatetraingene_data： 将属于同一个细菌（同一个ac）的genename放入同一个txt
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
    fout = open("genename_ac-np.txt", "w")
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
        fout.write(line[1]+" "+line[0]+"\n")
    fout.close()
    return NClist

def generatetraingene_data(allBacterials, acNameFile):
    fr1 = open(allBacterials, 'r')
    fr2 = open(acNameFile, 'r')
    acNameLists = []
    for line in fr2.readlines():
        acNameLists.append(line.strip().split(","))

    for line in fr1.readlines():
        #print(line)
        line = line.strip().split(",")
        print(line[2])
        fw = open(line[2] + "_np.txt", "w")
        #fw = open(line[2] + "_p.txt.", "w")
        for item in acNameLists:
            #print(item)
            print(line[2], item[1])
            if line[2] == item[1]:
                print(item[1])
                fw.write(item[0]+"\n")
        fw.close()
    fr1.close()
    fr2.close()

if __name__ == "__main__":
    #filepath = sys.argv[0]
    #NClist = geneac_genename("D://zola_workspace//worklab//entropyproject//essentialgene_dataset//deg-p-15.2//degannotation-p.dat")
    #NClist = genename_geneac("D://zola_workspace//worklab//entropyproject//essentialgene_dataset//deg-np-15.2//degannotation-np.dat")
    #print NClist
    generatetraingene_data("15bacterial-np.txt", "genename_ac-np.txt")
