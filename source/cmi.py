# -*- coding:utf-8 -*-

import mi
import math
import numpy as np

def createDouble(List1):
    List2 = []
    for i in range(len(List1)):
        for j in range(len(List1)):
            item = List1[i] + List1[j]
            List2.append(item)
    return List2


def createTrip(List1):
    trip = []
    for i in range(len(List1)):
        for j in range(len(List1)):
            for k in range(len(List1)):
                item = List1[i] + List1[j] + List1[k]
                trip.append(item)
    return trip

def computeProb(chain, subSeqList, delta=0.):
    prob = {}
    length = len(subSeqList[0])
    #print length, len(chain) - length + 1

    for item in subSeqList:
        count = chain.count(item)
        prob[item] = float("%.4f" % ((count + delta) / (len(chain) - length + 1 + 4 * delta)))

    return prob

def compute_cmi(tri_prob, di_nucleotides, nucleotides, delta=0.001):
    tri_items = tri_prob.keys()
    cmi_list = []
    for tri_item in tri_items:
        if(tri_prob[tri_item] == 0.0):
            cmi_list.append(0.0)
        else:
            z = tri_item[2]
            xz = tri_item[0]+z
            yz = tri_item[1:]
            p_tri = tri_prob[tri_item]
            cmi_value = p_tri * math.log((nucleotides[z]*p_tri+delta) / (di_nucleotides[xz]*di_nucleotides[yz]+delta),2)
            cmi_list.append(cmi_value)
    cmi_list.append(np.sum(cmi_list))
    return cmi_list

def cmi(chain):
    List1 = ["A", "T", "G", "C"]
    List2 = createDouble(List1)
    List3 = createTrip(List1)

    prob1 = computeProb(chain, List1)
    prob2 = computeProb(chain, List2)
    prob3 = computeProb(chain, List3)
    #print(prob1)
    #print(prob2)
    cmi_values = compute_cmi(prob3, prob2, prob1)
    print "cmi_values is: %s" %cmi_values
    return cmi_values

if __name__ == "__main__":
    sequence = "TACTTTTGTGAATTTCATCAACGATGTGGTTAACCATTATAAGTTCTCTATTCACTTTCTCGATTTTTTCGCAATGTTCTAACACTTCACAATAAGACACTTCTATCATCTCATTGTTCTTTTTACGACCTAAATGAGTTGTAACTAACGTTCGTTTTTTTCAAACAATAATTGTTGTCAAAATTTCTTTTTGTCTTAAATTGAAAACGACTCCTTAAATATTGATTGAAATTCACAACAGAACAATCACTACGTCCAATAGGATCAAATAGACTAGGACCATTACTTTACTAATTAACCTAGTATAGTTTTTTATTCCTCTATTCTTAGCTTCAATAATTACCAGGATCACGTAATTACACACCTAACTAGTGATCACCAAAATTTTGTTGTGGTGAAAACAAAAATCCAAAAAATTCAGTGTTTGTTTTAGTCGAGTTTTTAATAAATTCATGGATAGTTTTAGTCTTTTCGTGATAGCAAAAAAAACTTCGTCACGTATCCAATCTTTTATGAAATCTTTGACACTTTTTACAAAAATTTTTGTTACTGCAAAAATATCCTTCTCTTAATTGATTCAATGTACTTAGTGTAATAACTAAATTGTGGTCACTTTTGTGAAATGGACTGTAGTGAAATTTTCCTCTTAAACATTAACAATAACTATTAGTTTTATAATTAGTGGTTTGTAATAGAAGGTTAGTTATGAATCATATACTTTATTTCTTCAATTACCTATAACCACAATTCAATTTTCTACGTACGTTAATAAATCGATTTTTTTACGTAAATTTTAGTTCATACGAGATATGTGAAAAGGTACTTTCATAAATT"
    cmi_value = cmi(sequence)
    print "length of cmi: %d" %len(cmi_value)
