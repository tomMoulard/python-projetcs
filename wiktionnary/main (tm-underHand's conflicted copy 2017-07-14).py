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
    """
    print("Getting data from {}".format(url))
    res         = []
    site        = str(opener.open(url).read())
    soup        = BeautifulSoup(site, "html5lib")
    # content   = soup.find(id="mw-content-text")
    # headlines = content.select("span.mw-headline")
    posIntymo   = 0
    ymo         = soup.find_all("dl")
    posInol     = 0
    ol          = soup.find_all("ol")
    posInul     = 0
    ul          = soup.find_all("ul")
    dl          = soup.find_all("dl")
    posInboite  = 0
    boite       = soup.find_all("div", class_="boite")
    headlines   = soup.select("span.mw-headline")
    for headline in headlines:
        res.append(headline.text)
        if headline.text == "\\xc3\\x89tymologie":
            res.append(str(ymo[posIntymo]))
            posIntymo += 1
        elif headline.text == "Verbe":
            res.append(str(ol[posInol]))
            posInol += 1
        elif headline.text == "D\\xc3\\xa9riv\\xc3\\xa9s":
            res.append(str(boite[posInboite]))
            posInboite += 1
        elif headline.text == "Traductions" or\
            headline.text == "Traductions \\xc3\\xa0 trier":
            res.append(str(boite[posInboite]))
            posInboite += 1
        elif headline.text == "Prononciation":
            res.append(str(ul[posInul]))
            posInul += 1
        elif headline.text == "Anagrammes":
            res.append(str(ul[posInul]))
            posInul += 1
        elif headline.text == "R\\xc3\\xa9f\\xc3\\xa9rences":
            res.append(str(ul[posInul]))
            posInul += 1
        elif headline.text == "Variantes":
            res.append(str(ul[posInul]))
            posInul += 1
        elif headline.text == "Synonymes":
            tmp = ""
            for x in dl:
                tmp += str(x)
            res.append(tmp)
        else:
            pass
    return res

def getResponceNoms(url) :
    """
    To parse the response about a "Noms" word
    use : provide a good link to get the right type ("Noms") of word
    """
    print("Getting data from {}".format(url))
    res = []
    site         = str(opener.open(url).read())
    soup         = BeautifulSoup(site, "html5lib")
    # content    = soup.find(id="mw-content-text")
    # headlines  = content.select("span.mw-headline")
    posIntymo    = 0
    ymo          = soup.find_all("dl")
    posInol      = 0
    ol           = soup.find_all("ol")
    posInul      = 0
    ul           = soup.find_all("ul")
    posIndl      = 0
    dl           = soup.find_all("dl")
    posIntableNC = 0
    tableNC      = soup.find_all("table", class_="flextable flextable-fr-mfsp")
    posInboite   = 0
    boite        = soup.find_all("div", class_="boite")
    headlines    = soup.select("span.mw-headline")
    for headline in headlines:
        res.append(headline.text)
        if headline.text == "\\xc3\\x89tymologie":
            res.append(str(dl[posIndl]))
            posIndl += 1
        elif headline.text == "Nom commun":
            tmp = ""
            for table in tableNC:
                tmp += str(table)
            tmp     +=  str(ol[posInol])
            posInol += 1
            res.append(tmp)
        elif headline.text == "Note":
            res.append(str(ul[posInul]))
            posInul += 1
        elif headline.text == "D\\xc3\\xa9riv\\xc3\\xa9s":
            res.append(str(boite[posInboite]))
            posInboite += 1
        elif headline.text == "Expressions":
            res.append(str(ul[posInul]))
            posInul += 1
        elif headline.text == "Vocabulaire apparent\\xc3\\xa9 par le sens":
            res.append(str(ul[posInul]))
            posInul += 1
        elif headline.text == "Hyponymes":
            res.append(str(ul[posInul]))
            posInul += 1
        elif headline.text == "M\\xc3\\xa9ronymes":
            res.append(str(ul[posInul]))
            posInul += 1
        elif headline.text == "Traductions":
            res.append(str(boite[posInboite]))
            posInboite += 1
        elif headline.text == "Forme de verbe":
            tmp = ""
            for x in soup.find_all("table", class_="flextable"):
                tmp += str(x)
            res.append(tmp)
        elif headline.text == "Prononciation":
            tmp = str(ol[posInol])
            posInol += 1
            tmp += str(ul[posInul])
            res.append(tmp)
            posInul += 1
        elif headline.text == "Anagrammes":
            tmp = str(ul[posInul])
            posInul += 1
        elif headline.text == "Voir aussi":
            tmp = str(ul[posInul])
            posInul += 1
        elif headline.text == "R\\xc3\\xa9f\\xc3\\xa9rences":
            tmp = str(ul[posInul])
            posInul += 1
        else:
            pass
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