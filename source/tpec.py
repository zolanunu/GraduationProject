# -*- coding:utf-8 -*-
# calculate the topological entropy

import math
import re


def tpec(w, k):
    w_len = len(w)
    nw = int(math.floor(math.log(w_len - 1, 4)))
    subw = w[0:(4 ** nw) + nw - 1]
    if k > nw:
        return [1.0]
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
    return [gtecvalue]

if __name__ == "__main__":
    sequence = "TACTTTTGTGAATTTCATCAACGATGTGGTTAACCATTATAAGTTCTCTATTCACTTTCTCGATTTTTTCGCAATGTTCTAACACTTCACAATAAGACACTTCTATCATCTCATTGTTCTTTTTACGACCTAAATGAGTTGTAACTAACGTTCGTTTTTTTCAAACAATAATTGTTGTCAAAATTTCTTTTTGTCTTAAATTGAAAACGACTCCTTAAATATTGATTGAAATTCACAACAGAACAATCACTACGTCCAATAGGATCAAATAGACTAGGACCATTACTTTACTAATTAACCTAGTATAGTTTTTTATTCCTCTATTCTTAGCTTCAATAATTACCAGGATCACGTAATTACACACCTAACTAGTGATCACCAAAATTTTGTTGTGGTGAAAACAAAAATCCAAAAAATTCAGTGTTTGTTTTAGTCGAGTTTTTAATAAATTCATGGATAGTTTTAGTCTTTTCGTGATAGCAAAAAAAACTTCGTCACGTATCCAATCTTTTATGAAATCTTTGACACTTTTTACAAAAATTTTTGTTACTGCAAAAATATCCTTCTCTTAATTGATTCAATGTACTTAGTGTAATAACTAAATTGTGGTCACTTTTGTGAAATGGACTGTAGTGAAATTTTCCTCTTAAACATTAACAATAACTATTAGTTTTATAATTAGTGGTTTGTAATAGAAGGTTAGTTATGAATCATATACTTTATTTCTTCAATTACCTATAACCACAATTCAATTTTCTACGTACGTTAATAAATCGATTTTTTTACGTAAATTTTAGTTCATACGAGATATGTGAAAAGGTACTTTCATAAATT"
    print tpec(sequence, 3)
