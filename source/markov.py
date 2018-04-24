# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 14:31:46 2018

@author: liudiwei
"""
from random import randint
import math

def makeDict(text):
    #替换换行符和引号
    text = text.replace('\n', ' ')
    text = text.replace('\“', '')
    text = text.replace('\”', '')

    punc = ['，', '。', '？', '；', ':', '!']
    for symbol in punc:
        text = text.replace(symbol, ' '+symbol+' ')

    words = [word for word in text if word != '']

    wordict = {}
    for i in range(1, len(text)):
        if words[i-1] not in wordict:
            wordict[words[i-1]] = {}
        if words[i] not in wordict[words[i-1]]:
            wordict[words[i-1]][words[i]] = 0
        wordict[words[i-1]][words[i]] += 1

    return wordict


def wordLen(wordict):
    sum = 0
    for key, value in wordict.items():
        sum += value
    return sum

def retriveRandomWord(wordict):
    """
    计算每个单词的机率
    :param wordict:
    :return:
    """
    randindex = randint(1, wordLen(wordict))
    for key, value in wordict.items():
        randindex -= value
        if randindex <= 0:
            return key


def generateNextText(inputFile, outputFile, outLen=100):
    with open(inputFile,'r') as f:
        t = f.read()
    
    print t
    text = str(t)
    wordict = makeDict(text)

    chain = ''
    currentword = text[-1]
    print currentword
    for i in range(0, outLen):
        chain += currentword
        currentword = retriveRandomWord(wordict[currentword])

    with open(outputFile,'w') as file:
        file.write(chain)
    return chain


def generateNextChain(chain, outLen=200):
    wordict = makeDict(chain)
    currentword = chain[-1]
    print currentword
    for i in range(0, outLen):
        chain += currentword
        currentword = retriveRandomWord(wordict[currentword])
    return chain

def computeProb(chain, subSeq, delta = 0.001):
    preSubSeq = subSeq[0:-1]
    countPreSubSeq = chain.count(preSubSeq)
    countSubSeq = chain.count(subSeq)
    #print "countPreSubSeq: %d , countSubSeq: %d" %(countPreSubSeq, countSubSeq)
    prob = (countSubSeq + delta) / (countPreSubSeq + 4 * delta)
    return float("%.4f" % prob)

def getMarkovScore(seq, m = 1, netxtLength=100, delta = 0.001):
    chain = generateNextChain(seq, netxtLength)

    L = len(chain)
    score = 0.
    for i in range(0, (L - m + 1)):
        subSeq = chain[i:i+m]
        subScore = computeProb(chain, subSeq)
        probUp = computeProb(chain, subSeq[0:-1]) * subScore
        probDown = (chain.count(subSeq[-1]) + delta)/ (L + 4 * delta)
        score += subScore * math.log(probUp / probDown, 2)
        print score
    return [score]
    
if __name__ == "__main__":
    chain = generateNextText("test.txt", "res.txt", 200)
    print chain
    score = getMarkovScore(chain, 1)
    print score