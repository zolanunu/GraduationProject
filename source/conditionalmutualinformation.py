# -*- coding:utf-8 -*-

import mutualinformation
import math

def condon_dis(sequence):
    condon_distribution = {}
    seq_length = len(sequence)
    for i in range(seq_length -2):
        condon= sequence[i:i+3]
        if condon not in condon_distribution.keys():
            condon_distribution[condon] = 1
        else:
            condon_distribution[condon] += 1
    for item in condon_distribution.keys():
        condon_distribution[item] /= float(seq_length-2)
    print(len(condon_distribution.keys()))
    return condon_distribution

def cmi(condon_distribution, di_nucleotides, nucleotides):
    condon = condon_distribution.keys()
    condonvalue = {}
    for item in condon:
        xyz = (nucleotides[item[2]] * condon_distribution[item])/(di_nucleotides[item[1:]]*di_nucleotides[item[0:2:]])
        value = condon_distribution[item]*math.log(xyz, 2)
        condonvalue[item] = value
    value = 0.0
    for item in condonvalue.keys():
        value += condonvalue[item]
        condonvalue["thr"] = value
    return condonvalue

if __name__ == "__main__":
    sequence = "TACTTTTGTGAATTTCATCAACGATGTGGTTAACCATTATAAGTTCTCTATTCACTTTCTCGATTTTTTCGCAATGTTCTAACACTTCACAATAAGACACTTCTATCATCTCATTGTTCTTTTTACGACCTAAATGAGTTGTAACTAACGTTCGTTTTTTTCAAACAATAATTGTTGTCAAAATTTCTTTTTGTCTTAAATTGAAAACGACTCCTTAAATATTGATTGAAATTCACAACAGAACAATCACTACGTCCAATAGGATCAAATAGACTAGGACCATTACTTTACTAATTAACCTAGTATAGTTTTTTATTCCTCTATTCTTAGCTTCAATAATTACCAGGATCACGTAATTACACACCTAACTAGTGATCACCAAAATTTTGTTGTGGTGAAAACAAAAATCCAAAAAATTCAGTGTTTGTTTTAGTCGAGTTTTTAATAAATTCATGGATAGTTTTAGTCTTTTCGTGATAGCAAAAAAAACTTCGTCACGTATCCAATCTTTTATGAAATCTTTGACACTTTTTACAAAAATTTTTGTTACTGCAAAAATATCCTTCTCTTAATTGATTCAATGTACTTAGTGTAATAACTAAATTGTGGTCACTTTTGTGAAATGGACTGTAGTGAAATTTTCCTCTTAAACATTAACAATAACTATTAGTTTTATAATTAGTGGTTTGTAATAGAAGGTTAGTTATGAATCATATACTTTATTTCTTCAATTACCTATAACCACAATTCAATTTTCTACGTACGTTAATAAATCGATTTTTTTACGTAAATTTTAGTTCATACGAGATATGTGAAAAGGTACTTTCATAAATT"
    condon_dis = condon_dis(sequence)
    di_nus = mutualinformation.pairrepeatenumber(sequence)
    nus = mutualinformation.entropy(sequence)
    condon_value = cmi(condon_dis, di_nus, nus)
    print(condon_value)