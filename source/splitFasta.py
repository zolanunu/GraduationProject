# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 19:23:31 2018

@author: liudiwei
"""
import os

def splitFasta(fasta, outdir):
    if os.path.exists(outdir):
        os.removedirs(outdir)
    os.makedirs(outdir)

    fr = open(fasta, "r")
    content = ""

    geneName = ""
    for eachline in fr.readlines():
        if ">" in eachline:
            if content != "":
                filename = geneName
                fw = open(outdir + "/" + filename[1:-1], "w")
                fw.write(geneName + content)
                fw.close()

            geneName = eachline
            content = ""
            continue
        content += eachline.strip()
    filename = geneName
    fw = open(outdir + "/" + filename[1:-1], "w")
    fw.write(geneName + content)
    fw.close()
    fr.close()

if __name__ == "__main__":
    splitFasta("fasta.txt", "outdir")
