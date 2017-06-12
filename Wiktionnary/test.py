import urllib.request
opener = urllib.request.FancyURLopener({})

from bs4 import BeautifulSoup
res = []
url = "https://fr.wiktionary.org/wiki/baleine"

def pp(l):
    for x in l:
        print([x])
    print(len(l))



print("Getting data from {}".format(url))
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
posIndl     = 0
dl          = soup.find_all("dl")
posIntableNC = 0
tableNC       = soup.find_all("table", class_="flextable flextable-fr-mfsp")
posInboite  = 0
boite       = soup.find_all("div", class_="boite")

headlines   = soup.select("span.mw-headline")
for headline in headlines:
    res.append(headline.text)
    if headline.text == "\\xc3\\x89tymologie":
        res.append(str(dl[posIntdl]))
        posIntdl += 1
    elif headline.text == "Nom commun":
        tmp = ""
        for table in tableNC:
            tmp += str(table)
        tmp     +=  str(ol[posInol])
        posInol += 1
        res.append(tmp)


    else:
        pass


pp(res)

"""[
    'Fran\\xc3\\xa7ais', 
    '\\xc3\\x89tymologie', 
    'Nom commun', 
    'Note', 
    'D\\xc3\\xa9riv\\xc3\\xa9s', 
    'Expressions', 
    'Vocabulaire apparent\\xc3\\xa9 par le sens', 
    'Hyponymes', 
    'M\\xc3\\xa9ronymes', 
    'Traductions', 
    'Forme de verbe', 
    'Prononciation', 
    'Homophones', 
    'Anagrammes', 
    'Voir aussi', 
    'R\\xc3\\xa9f\\xc3\\xa9rences', 
    'Ancien fran\\xc3\\xa7ais', 
    'Nom commun', 
]"""