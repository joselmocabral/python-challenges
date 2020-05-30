#Given an array, find the integer that appears an odd number of times.

#There will always be only one integer that appears an odd number of times.

from itertools import groupby

def find_it(seq):
    seq.sort()
    seq2 = [list(g) for k, g in groupby(seq)]
    pos = [len(x)%2 for x in seq2]
    return seq2[pos.index(1)][0]
