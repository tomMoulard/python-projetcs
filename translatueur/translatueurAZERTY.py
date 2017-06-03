"""
This was made for a funky way of translating things
"""

import sys

letters = {
    "z" : "a",
    "e" : "z",
    "r" : "e",
    "t" : "r",
    "y" : "t",
    "u" : "y",
    "i" : "u",
    "o" : "i",
    "p" : "o",
    "a" : "p",
    "s" : "q",
    "d" : "s",
    "f" : "d",
    "g" : "f",
    "h" : "g",
    "j" : "h",
    "k" : "j",
    "l" : "k",
    "m" : "l",
    "q" : "m",
    "x" : "w",
    "c" : "x",
    "v" : "c",
    "b" : "v",
    "n" : "b",
    "w" : "n",
    "." : ".",
    "_" : "_",
}

def trans(name):
    res = ""
    for letter in name:
        res += letters[letter]
    return res

def main():
    if len(sys.argv) < 2:
        print("usage: python3 translatueurAZERTY.py <nameToTransalte>*")
    nameToTransalte = sys.argv[1:]
    for name in nameToTransalte:
        name = name.casefold()
        print("{} -> {}".format(name, trans(name)))

if __name__ == '__main__':
    main()