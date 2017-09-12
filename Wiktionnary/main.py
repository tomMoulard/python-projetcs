# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 23:07:26 2017

@author: tm
Main Goal: Parce a wikipedia page to get all words in it and their links to theirs page.
After we need to go on each pages and get all the data possible
"""

#To get the http response for files
import urllib.request
opener = urllib.request.FancyURLopener({})

#To get users imput
import sys

#To get full lenght urls
prefix = "https://fr.wiktionary.org/wiki/"

#To edit xlsx files
import xlsxwriter

#To parse all pages
from bs4 import BeautifulSoup

def prettyPrintForList(l):
    """
    This is a function to do some pretty print for list
    """
    for x in l:
        print(x)

def getResponceVerbe(url) :
    """
    To parse the response about a "Verbe" word
    use : provide a good link to get the right type ("Verbe") of word
    format: [[headlines, "", content]]
    like: [[h1, h2, h3, "", c1, c2, c3]]
    """
    res = []
    # response = str(opener.open(url).read())
    # ll, pos = len(response), 0
    # while pos < ll:
    #     pos += 1
    print("Getting data from {}".format(url))
    site = str(opener.open(url).read())
    soup = BeautifulSoup(site, "html5lib")
    content = soup.find(id="mw-content-text")
    headlines = content.select("span.mw-headline")
    for headline in headlines:
        res.append(headline.text)
    res.append("")


    return res

def getResponceNoms(url) :
    """
        To parse the response about a "Noms" word
    use : provide a good link to get the right type ("Noms") of word
    """
    res = []
    # response = str(opener.open(url).read())
    # ll, pos = len(response), 0
    # while pos < ll:
    #     pos += 1
    return res;

def getResponceAdjectifs(url) :
    """
    To parse the response about a "Adjectif" word
    use : provide a good link to get the right type ("Adjectif") of word
    """
    res = []
    # response = str(opener.open(url).read())
    # ll, pos = len(response), 0
    # while pos < ll:
    #     pos += 1
    return res;

def getResponceAdverbes(url) :
    """
    To parse the response about a "Adverbe" word
    use : provide a good link to get the right type ("Adverbe") of word
    """
    res = []
    # response = str(opener.open(url).read())
    # ll, pos = len(response), 0
    # while pos < ll:
    #     pos += 1
    return res;

def getResponcePrepositions(url) :
    """
    To parse the response about a "Préposition" word
    use : provide a good link to get the right type ("Préposition") of word
    """
    res = []
    # response = str(opener.open(url).read())
    # ll, pos = len(response), 0
    # while pos < ll:
    #     pos += 1
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
        response = str(opener.open(url).read())
        #print(response)
        print("Main Responce get")
        #curl link
        urls = []
        pos  = 0
        ll   = len(response)
        tag  = "Noms"
        while pos < ll - 6:
            if response[pos:pos + 6] == "/wiki/" and \
            (response[pos + 6] != "w" and response[pos + 7] != "i"):
                pos += 6
                link = prefix
                while pos < ll and response[pos] != "\"":
                    link += response[pos]
                    pos  += 1
                pos += 9
                title = ""
                while pos < ll and response[pos] != "\"":
                    title += response[pos]
                    pos += 1
                #print(title, ": ", tag)
                urls.append((title ,link, tag, []))
            # The next part is to define the tag for next words
            if response[pos:pos + 5] == "Verbe":
                tag = "Verbe"
            if response[pos:pos + 4] == "Noms":
                tag = "Noms"
            if response[pos:pos + 9] == "Adjectifs":
                tag = "Adjectifs"
            if response[pos:pos + 8] == "Adverbes":
                tag = "Adverbes"
            if response[pos:pos + 19] == "Pr\xc3\xa9positions":
                tag = "Prépositions"
                print("Pr\xc3\xa9positions")
            pos += 1
        #just for fun making it in the file
        urls = urls[:-15]
        #opening the file :
        print("Writting links to {}".format(file))
        workbook  = xlsxwriter.Workbook(file)
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold': True})
        for x in range(len(urls)):
            worksheet.write(x, 0, urls[x][0]) #TITLE
            worksheet.write(x, 1, urls[x][1]) #LINK
            worksheet.write(x, 2, urls[x][2]) #TAG
        workbook.close()
        print("File Closed")

        n = input("Do you want to get the whole data ? [Y/n]")
        if n == "n":
            exit(0)
        #Lets get all the data
        #open all page and parse the output to get the data
        for x in range(len(urls)):
            if x % 10 == 0:
                print("Got response for", x, "words.")
            if urls[x][2] == "verbe":
                print("supposed to be {} but is really ->".format("verbe"), [urls[x][2]], "verbe" == urls[x][2])
                urls[x] = (urls[x][0], urls[x][1], urls[x][2], getResponceVerbe(urls[x][1]))
            elif urls[x][2] == "Noms":
                print("supposed to be {} but is really ->".format("Noms"), [urls[x][2]], "Noms" == urls[x][2])
                urls[x] = (urls[x][0], urls[x][1], urls[x][2], getResponceNoms(urls[x][1]))
            elif urls[x][2] == "Adjectifs":
                print("supposed to be {} but is really ->".format("Adjectifs"), [urls[x][2]], "Adjectifs" == urls[x][2])
                urls[x] = (urls[x][0], urls[x][1], urls[x][2], getResponceAdjectifs(urls[x][1]))
            elif urls[x][2] == "Adverbes":
                print("supposed to be {} but is really ->".format("Adverbes"), [urls[x][2]], "Adverbes" == urls[x][2])
                urls[x] = (urls[x][0], urls[x][1], urls[x][2], getResponceAdverbes(urls[x][1]))
            else:
                print("supposed to be {} but is really ->".format("else"), [urls[x][2]], "else" == urls[x][2])
                #getResponcePrepositions
                urls[x] = (urls[x][0], urls[x][1], urls[x][2], getResponceVerbe(urls[x][1]))
        #write the output to xlsx
        print("Writting data to {}".format(file))
        workbook  = xlsxwriter.Workbook(file)
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold': True})
        for x in range(len(urls)):
            worksheet.write(x, 0, urls[x][0]) #TITLE
            worksheet.write(x, 1, urls[x][1]) #LINK
            worksheet.write(x, 2, urls[x][2]) #TAG
            for y in range(len(urls[x][3])):
                worksheet.write(x, y + 3, urls[x][3][y]) #STUFF
        workbook.close()
        print("File Closed")

if __name__ == '__main__':
    main()