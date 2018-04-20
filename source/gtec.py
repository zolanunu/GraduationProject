# -*- coding: utf-8 -*-

import re
import math


def topologicalentropy(w, k):
    """

    :param w:
    :param k:
    :return:
    """
    w = w.strip(' ')
    w_len = len(w)
    nw = 0
    if w_len > 30000:
        return 1.0
    nw = int(math.floor(math.log(w_len, 4)))
    sub_w = w[0:(4 ** nw) + nw]
    sub_w_len = len(sub_w)
    if ((k < 0 or k > nw) or (w_len >= ((4 ** (nw + 1)) + (nw + 1) - 1)) or (w_len < (4 ** nw + nw - 1))):
        return 1.0
    # print(sub_w_len)
    ssum = 0.0000001
    for i in range(nw - k + 1, nw + 1):
        subset = set()
        pwi = 0
        ai = 0.0
        for j in range(0, sub_w_len - i + 1):
            subset.add(sub_w[j:j + i])
        pwi = len(subset)
        ai = ((math.log(pwi, 4)) / i)
        ssum += ai
    topologicalentropyvalue = ssum / k
    return topologicalentropyvalue


if __name__ == "__main__":
    pass
