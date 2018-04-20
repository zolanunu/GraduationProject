# -*- coding:utf-8 -*-
import math
import collections
def pairrepeatenumber(seq):
    di_nucleotides = {}
    for i in range(len(seq) - 1):
        di_seq = seq[i:i + 2]
        if di_seq not in di_nucleotides.keys():
            di_nucleotides[di_seq] = 1
        else:
            di_nucleotides[di_seq] += 1
    for item in di_nucleotides.keys():
        di_nucleotides[item] /= float(len(sequence)-1)
    print(len(di_nucleotides.keys()))
    return di_nucleotides


def entropy(seq):
    nucleotide_dict = {'A': 0, 'G': 0, 'C': 0, 'T': 0}
    for i in range(len(seq)):
        nucleotide_dict[seq[i]] += 1
    print(nucleotide_dict)
    for item in nucleotide_dict.keys():
        nucleotide_dict[item] /= float(len(seq))
    #print(nucleotide_dict)
    return nucleotide_dict

def mi(nucleotides, di_nucleotides):
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
                mi[seq] = di_nucleotides[seq] * math.log((di_nucleotides[seq]/(nucleotides[item1]*nucleotides[item2])))
            else:
                mi[seq] = 0.0
    value = 0.0
    print(seqs)
    for item in mi.keys():
        value += mi[item]
    mi["di_nucleotides"] = value
    print(len(mi), mi)
    return mi
import json
if __name__ == "__main__":
    sequence = "TACTTTTGTGAATTTCATCAACGATGTGGTTAACCATTATAAGTTCTCTATTCACTTTCTCGATTTTTTCGCAATGTTCTAACACTTCACAATAAGACACTTCTATCATCTCATTGTTCTTTTTACGACCTAAATGAGTTGTAACTAACGTTCGTTTTTTTCAAACAATAATTGTTGTCAAAATTTCTTTTTGTCTTAAATTGAAAACGACTCCTTAAATATTGATTGAAATTCACAACAGAACAATCACTACGTCCAATAGGATCAAATAGACTAGGACCATTACTTTACTAATTAACCTAGTATAGTTTTTTATTCCTCTATTCTTAGCTTCAATAATTACCAGGATCACGTAATTACACACCTAACTAGTGATCACCAAAATTTTGTTGTGGTGAAAACAAAAATCCAAAAAATTCAGTGTTTGTTTTAGTCGAGTTTTTAATAAATTCATGGATAGTTTTAGTCTTTTCGTGATAGCAAAAAAAACTTCGTCACGTATCCAATCTTTTATGAAATCTTTGACACTTTTTACAAAAATTTTTGTTACTGCAAAAATATCCTTCTCTTAATTGATTCAATGTACTTAGTGTAATAACTAAATTGTGGTCACTTTTGTGAAATGGACTGTAGTGAAATTTTCCTCTTAAACATTAACAATAACTATTAGTTTTATAATTAGTGGTTTGTAATAGAAGGTTAGTTATGAATCATATACTTTATTTCTTCAATTACCTATAACCACAATTCAATTTTCTACGTACGTTAATAAATCGATTTTTTTACGTAAATTTTAGTTCATACGAGATATGTGAAAAGGTACTTTCATAAATT"
    di_nus = pairrepeatenumber(sequence)
    print(len(sequence))
    nus = entropy(sequence)
    print(len(di_nus))
    midict = mi(nus, di_nus)
    jsons = json.dumps(midict)
    print(type(jsons))
