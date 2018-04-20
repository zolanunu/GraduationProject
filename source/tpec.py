# -*- coding:utf-8 -*-
# calculate the topological entropy

import math
import re


def topologicalentropy(w, k):
    w_len = len(w)
    nw = int(math.floor(math.log(w_len - 1), 4))
    subw = w[0:(4 ** nw) + nw - 1]
    if not nw <= k:
        return 1.0
    subwlen = len(subw)
    lk = []
    tpe = 0
    gtecvalue = 0
    for i in range(0, subwlen - k):
        if subw[i:i + k] not in lk:
            lk.append(subw[i:i + k])
    if len(lk) > 1:
        tpe = math.log(len(lk) - 1, 4)
    if k > 0:
        gtecvalue = tpe / k
    return gtecvalue


def format(filein, fileout):
    fr = open(filein)
    fw = open(fileout, 'w')
    lines = ''
    count = 0
    for line in fr.readlines():
        if re.match('>', line):
            fw.write(lines)
            fw.write("\n" + line)
            lines = ''
            if count > 100:
                break
        else:
            lines = lines + line.strip("\n")


if __name__ == "__main__":
    pass
