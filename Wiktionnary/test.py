import urllib.request
opener = urllib.request.FancyURLopener({})

from bs4 import BeautifulSoup
res = []
url = "https://fr.wiktionary.org/wiki/petit"

def pp(l):
    for x in l:
        print([x])
    print(len(l))



print("Getting data from {}".format(url))
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
    #     res.append(str(dl[posIndl]))
    #     posIndl += 1
    elif headline.text == "Adjectif":
    elif headline.text == "Variantes":
    elif headline.text == "D\\xc3\\xa9riv\\xc3\\xa9s dans d\\xe2\\x80\\x99autres langues":
    elif headline.text == "Synonymes":
    elif headline.text == "Antonymes":
    elif headline.text == "D\\xc3\\xa9riv\\xc3\\xa9s":
    elif headline.text == "Proverbes et phrases toutes faites":
    elif headline.text == "Traductions":
    elif headline.text == "Nom commun 1":
    elif headline.text == "Variantes dialectales":
    elif headline.text == "Nom commun 2":
    elif headline.text == "Adverbe":
    elif headline.text == "Expressions":
    elif headline.text == "Prononciation":
    elif headline.text == "Homophones":
    elif headline.text == "Voir aussi":
    elif headline.text == "R\\xc3\\xa9f\\xc3\\xa9rences":
    elif headline.text == "Ancien fran\\xc3\\xa7ais":
    elif headline.text == "Nom commun":
    elif headline.text == "Anagrammes":
    elif headline.text == "Catalan":
        



    else:
        pass


pp(res)
