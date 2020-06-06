from itertools import groupby
import re

def top_3_words(text):
    print(text)
    text = list(filter(lambda x: x!= '', re.split("[,.?!:_/;-]| |//|\n|'''", text)))
    text = list(map(lambda x: x.lower(), list(filter(lambda x: x!= "'", text))))
    grouped = [list(g) for k, g in groupby(sorted(text))]
    # grouped = sorted(grouped, key=lambda x: (x[0].lower(), x[0].swapcase()))
    grouped = list(map(lambda x: x[0], sorted(grouped, key = lambda x: len(x), reverse = True)))

    return grouped[:3]