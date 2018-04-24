# -*- coding:utf-8 -*-
import math


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

def computeProb(chain, subSeqList, delta = 0.):
    prob = {}
    length = len(subSeqList[0])
    print length, len(chain) - length + 1
    for item in subSeqList:
        count = chain.count(item)
        prob[item] = float("%.4f" %((count + delta) / (len(chain) - length + 1 + 4 * delta)))
    return prob

def computA(chain):
    probA = {}
    return probA

def computeB(chain):
    probB = {}
    return probB

def computeC(chain):
    probC = {}
    return probC

def computeKLD(probA={}, probB={}, delta = 0.001):
    score = 0.
    list1 = probA.keys()
    list2 = probB.keys()
    for i in range(len(list1)):
        for j in range(len(list2)):
            px = probA[list1[i]]
            qx = probB[list2[j]]
            score += px * math.log((px + delta) / (qx + 4*delta), 2)
    return score

def computeKLValue(chain):
    List1 = ["A", "T", "G", "C"]
    List2 = createDouble(List1)
    List3 = createTrip(List1)

    prob1 = computeProb(chain, List1)
    prob2 = computeProb(chain, List2)
    prob3 = computeProb(chain, List3)

    val1 = computeKLD(prob1, prob2)
    val2 = computeKLD(prob1, prob3)
    val3 = computeKLD(prob2, prob3)
    return  [val1, val2, val3]

if __name__ == "__main__":
    chain = "TACTTTTGTGAATTTCATCAACGATGTGGTTAACCATTATAAGTTCTCTATTCACTTTCTCGATTTTTTCGCAATGTTCTAACACTTCACAATAAGACACTTCTATCATCTCATTGTTCTTTTTACGACCTAAATGAGTTGTAACTAACGTTCGTTTTTTTCAAACAATAATTGTTGTCAAAATTTCTTTTTGTCTTAAATTGAAAACGACTCCTTAAATATTGATTGAAATTCACAACAGAACAATCACTACGTCCAATAGGATCAAATAGACTAGGACCATTACTTTACTAATTAACCTAGTATAGTTTTTTATTCCTCTATTCTTAGCTTCAATAATTACCAGGATCACGTAATTACACACCTAACTAGTGATCACCAAAATTTTGTTGTGGTGAAAACAAAAATCCAAAAAATTCAGTGTTTGTTTTAGTCGAGTTTTTAATAAATTCATGGATAGTTTTAGTCTTTTCGTGATAGCAAAAAAAACTTCGTCACGTATCCAATCTTTTATGAAATCTTTGACACTTTTTACAAAAATTTTTGTTACTGCAAAAATATCCTTCTCTTAATTGATTCAATGTACTTAGTGTAATAACTAAATTGTGGTCACTTTTGTGAAATGGACTGTAGTGAAATTTTCCTCTTAAACATTAACAATAACTATTAGTTTTATAATTAGTGGTTTGTAATAGAAGGTTAGTTATGAATCATATACTTTATTTCTTCAATTACCTATAACCACAATTCAATTTTCTACGTACGTTAATAAATCGATTTTTTTACGTAAATTTTAGTTCATACGAGATATGTGAAAAGGTACTTTCATAAATT"
    res1 = computeKLValue(chain)
    print res1
