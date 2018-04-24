# -*- coding:utf-8 -*-
import math
import collections
import json
import entropy

def pairRepeateNumber(seq):
    di_nucleotides = {}
    for i in range(len(seq) - 1):
        di_seq = seq[i:i + 2]
        if di_seq not in di_nucleotides.keys():
            di_nucleotides[di_seq] = 1
        else:
            di_nucleotides[di_seq] += 1
    for item in di_nucleotides.keys():
        di_nucleotides[item] /= float(len(seq)-1)
    #print(len(di_nucleotides.keys()))
    return di_nucleotides

def mi(nucleotides, di_nucleotides, delta=0.001):
    # type: (object, object) -> object
    """
    :type nucleotides: dict
    :type di_nucleotides: dict
    """
    keys = nucleotides.keys()
    seqs = []
    mi = collections.OrderedDict()
    for item1 in keys:
        for item2 in keys:
            seq = item1 + item2
            seqs.append(seq)
            if seq in di_nucleotides.keys():
                mi[seq] = di_nucleotides[seq] * math.log(((di_nucleotides[seq]+delta)/((nucleotides[item1]*nucleotides[item2])+delta)))
            else:
                mi[seq] = 0.0
    value = 0.0
    #print(seqs)
    for item in mi.keys():
        value += mi[item]
    mi["di_nucleotides"] = value
    #print(len(mi), mi)
    di_nucleotideslist = []
    for item in mi.keys():
        di_nucleotideslist.append(mi.get(item))
    return di_nucleotideslist

def computeMI(sequence):
    di_nus = pairRepeateNumber(sequence)
    nus, entropyDict = entropy.entropy(sequence)
    result = mi(entropyDict, di_nus)
    return result


if __name__ == "__main__":
    sequence = "TACTTTTGTGAATTTCATCAACGATGTGGTTAACCATTATAAGTTCTCTATTCACTTTCTCGATTTTTTCGCAATGTTCTAACACTTCACAATAAGACACTTCTATCATCTCATTGTTCTTTTTACGACCTAAATGAGTTGTAACTAACGTTCGTTTTTTTCAAACAATAATTGTTGTCAAAATTTCTTTTTGTCTTAAATTGAAAACGACTCCTTAAATATTGATTGAAATTCACAACAGAACAATCACTACGTCCAATAGGATCAAATAGACTAGGACCATTACTTTACTAATTAACCTAGTATAGTTTTTTATTCCTCTATTCTTAGCTTCAATAATTACCAGGATCACGTAATTACACACCTAACTAGTGATCACCAAAATTTTGTTGTGGTGAAAACAAAAATCCAAAAAATTCAGTGTTTGTTTTAGTCGAGTTTTTAATAAATTCATGGATAGTTTTAGTCTTTTCGTGATAGCAAAAAAAACTTCGTCACGTATCCAATCTTTTATGAAATCTTTGACACTTTTTACAAAAATTTTTGTTACTGCAAAAATATCCTTCTCTTAATTGATTCAATGTACTTAGTGTAATAACTAAATTGTGGTCACTTTTGTGAAATGGACTGTAGTGAAATTTTCCTCTTAAACATTAACAATAACTATTAGTTTTATAATTAGTGGTTTGTAATAGAAGGTTAGTTATGAATCATATACTTTATTTCTTCAATTACCTATAACCACAATTCAATTTTCTACGTACGTTAATAAATCGATTTTTTTACGTAAATTTTAGTTCATACGAGATATGTGAAAAGGTACTTTCATAAATT"
    print computeMI(sequence)