# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 23:07:26 2017

@author: tm
"""

#to get the http responce for files
import urllib.request
opener = urllib.request.FancyURLopener({})

#to get users imput
import sys

#To get full lenght urls
prefix = "https://fr.wiktionary.org/wiki/"

#to edit xlsx files
import xlsxwriter


def getResponceVerbe(url) : 
    """
    To parse the responce about a "Verbe" word
    use : provide a good link to get the right type ("Verbe") of word
    """
    res = []
    responce = str(opener.open(url).read())
    ll, pos = len(responce), 0
    while pos < ll:
        pos += 1
    return res;

def getResponceNoms(url) : 
    """
    To parse the responce about a "Noms" word
    use : provide a good link to get the right type ("Noms") of word
    """
    res = []
    responce = str(opener.open(url).read())
    ll, pos = len(responce), 0
    while pos < ll:
        pos += 1
    return res;

def getResponceAdjectifs(url) : 
    """
    To parse the responce about a "Adjectif" word
    use : provide a good link to get the right type ("Adjectif") of word
    """
    res = []
    responce = str(opener.open(url).read())
    ll, pos = len(responce), 0
    while pos < ll:
        pos += 1
    return res;

def getResponceAdverbes(url) : 
    """
    To parse the responce about a "Adverbe" word
    use : provide a good link to get the right type ("Adverbe") of word
    """
    res = []
    responce = str(opener.open(url).read())
    ll, pos = len(responce), 0
    while pos < ll:
        pos += 1
    return res;

def getResponcePrepositions(url) : 
    """
    To parse the responce about a "Préposition" word
    use : provide a good link to get the right type ("Préposition") of word
    """
    res = []
    responce = str(opener.open(url).read())
    ll, pos = len(responce), 0
    while pos < ll:
        pos += 1
    return res;


def main():
    """
    input be like : "python3 main.py https://fr.wiktionary.org/wiki/Wiktionnaire:Liste_de_1750_mots_fran%C3%A7ais_les_plus_courants output.xlsx"
    aka : "python3 main.py <link> <output file>.xlsx"
    """
    if(len(sys.argv) != 3):
        print("Bad input, try : \npython3 main.py <link> <output file>.xlsx")
    else:
        url      = sys.argv[1]
        file     = sys.argv[2]
        responce = str(opener.open(url).read())
        #print(responce)
        print("Main Responce get")
        #curl link
        urls = []
        pos  = 0
        ll   = len(responce)
        tag  = "Noms"
        while pos < ll - 6:
            if responce[pos:pos + 6] == "/wiki/" and \
            (responce[pos + 6] != "w" and responce[pos + 7] != "i"):
                pos += 6
                link = prefix
                while pos < ll and responce[pos] != "\"":
                    link += responce[pos]
                    pos  += 1
                pos += 9
                title = ""
                while pos < ll and responce[pos] != "\"":
                    title += responce[pos]
                    pos += 1
                #print(title, ": ", tag)
                urls.append((title ,link, tag, []))
            if responce[pos:pos + 5] == "Verbe":
                tag = "Verbe"
            if responce[pos:pos + 4] == "Noms":
                tag = "Noms"
            if responce[pos:pos + 9] == "Adjectifs":
                tag = "Adjectifs"
            if responce[pos:pos + 8] == "Adverbes":
                tag = "Adverbes"
            if responce[pos:pos + 19] == "Pr\xc3\xa9positions":
                tag = "Prépositions"
                print("Pr\xc3\xa9positions")
            pos += 1
        print("links get")
        for x in range(len(urls) - 15):
            if x % 10 == 0:
                print("Got responce for", x, "words.")
            if urls[x][2] == "verbe":
                pass
                #urls[x] = (urls[x][0], urls[x][1], urls[x][2], getResponceVerbe(urls[x][1]))
            elif urls[x][2] == "Noms":
                pass
                #urls[x] = (urls[x][0], urls[x][1], urls[x][2], getResponceNoms(urls[x][1]))
            elif urls[x][2] == "Adjectifs":
                pass
                #urls[x] = (urls[x][0], urls[x][1], urls[x][2], getResponceAdjectifs(urls[x][1]))
            elif urls[x][2] == "Adverbes":
                pass
                #urls[x] = (urls[x][0], urls[x][1], urls[x][2], getResponceAdverbes(urls[x][1]))
            elif urls[x][2] == "Prépositions":
                pass
                #urls[x] = (urls[x][0], urls[x][1], urls[x][2], getResponcePrepositions(urls[x][1]))
            else:
                print("error:", x, urls[x])
        print("Got result for files")
        #just for fun making it in the file :3
        #opening the file :
        workbook  = xlsxwriter.Workbook(file)
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold': True})
        for x in range(len(urls) - 15):
            worksheet.write(x, 0, urls[x][0]) #TITLE
            worksheet.write(x, 1, urls[x][1]) #LINK
            worksheet.write(x, 2, urls[x][2]) #TAG
            for y in range(len(urls[x][3])):
                worksheet.write(x, y + 3, urls[x][3][y]) #STUFF
        workbook.close()
        print("File Closed")
        #parse responce to get all words links and store them in a list stored in a separated file
        #for each link get the http responce to get responce 
        #make an array of object with the world + definitions
        #store then in the xlsx file


if __name__ == '__main__':
    main()