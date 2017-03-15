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

def main():
    #get users input
    if(len(sys.argv) != 3):
        print("Bad input, try : \npython3 main.py <link> <output file>.xlsx")
    else:
        #input be like : "python3 main.py https://fr.wiktionary.org/wiki/Wiktionnaire:Liste_de_1750_mots_fran%C3%A7ais_les_plus_courants output.xlsx"
        #aka : "python3 main.py <link> <output file>.xlsx"
        url      = sys.argv[1]
        file     = sys.argv[2]
        responce = str(opener.open(url).read())
        print("Main Responce get :)")
        #curl link
        urls = []
        pos  = 0
        ll   = len(responce)
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
                urls.append((title ,link))
            pos += 1
        print("links get")
        #just for fun making it in the file :3
        #opening the file :
        workbook  = xlsxwriter.Workbook(file)
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold': True})
        for x in range(len(urls) - 15):
            worksheet.write(x, 0, urls[x][0], bold)
            worksheet.write(x, 1, urls[x][1])
        workbook.close()
        #parse responce to get all words links and store them in a list stored in a separated file
        #for each link get the http responce to get responce 
        #make an array of object with the world + definitions
        #store then in the xlsx file


if __name__ == '__main__':
    main()