# -*- coding: utf-8 -*-
"""
.srt File translator

Junuary 2018
@author: moular_b
"""
import sys
import re
import os
from translate import Translator

def translate(s, finalLang):
    print(s, "->", end=" ")
    res = os.popen("translate-cli -t {} \"{}\" -o".format(finalLang, s)).readlines()
    print(res)
    return res[0]

def main():
    args = sys.argv
    if len(args) < 3:
        print("Not enought args :/\nUse it like: \n\tpython3 translator.py <srt file> fr\nTo translate <srt file> to french")
        return 1
    translator = Translator(to_lang=args[2])
    with open(args[1], "r") as f:
        srtfile = f.read()
    srtfile = srtfile.split("\n")
    pos, ll = 0, len(srtfile)
    res = ""
    while srtfile[pos] == "" and pos < ll:
        pos += 1
    while pos + 2 < ll:
        res += str(srtfile[pos]) + "\n" + str(srtfile[pos + 1]) + "\n"
        pos += 2
        while srtfile[pos] != "" and pos < ll:
            # res += translate(str(srtfile[pos]), args[2]) + "\n" 
            print([srtfile[pos]], "->", end=" ")
            tmp = translator.translate(str(srtfile[pos]))
            print([tmp])
            res += tmp + "\n" 
            pos += 1
        res += "\n"
        pos += 1
    # print(res)

if __name__ == '__main__':
    main()