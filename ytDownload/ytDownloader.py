#made by TomMoulard

import urllib.request

def urlMaker(keywords): #make url to querry
	if len(keywords) < 1:
		print("Bad Input :/ \nTry again ...")
		main()
	q = "https://www.youtube.com/results?search_query="
	for x in range(len(keywords) - 1):
		q += keywords[x] + "+"
	q += keywords[len(keywords) - 1]
	return q

def getPageSource(url): #return source code to parse of the page
	opener = urllib.request.FancyURLopener({})
	res = opener.open(url).read().decode('utf-8')
	return res

def parsingPage(source): #parse the page and return potentilal urls
	urls =[]
	samp = "http://www.youtube.com/watch"
	sources = source.split("<a href=\"/watch")
	for x in sources:
		#to get the url of the page
		ls, posInX, found = len(x), 0, False
		resUrl = samp
		while not found and ls > posInX:
			tmp = x[posInX]
			if tmp == "\"":
				found = True
			else:
				resUrl += tmp
				posInX += 1
		#to get the title of the video
		y = x.split("title=\"")
		resTitle = ""
		if len(y) > 1:
			y = y[1]
			ly, posInY, found = len(y), 0, False
			while not found and posInY < ly:
				tmp = y[posInY]
				if tmp == "\"":
					found = True
				else:
					resTitle += tmp
					posInY += 1
		urls.append((resUrl, resTitle))
	del urls[0] 
	return urls

def printParsed(l):
	for x in l:
		print(x[0], x[1])


def makePoint(title, keywords):
	return 42 #point according to the subject....

def chooseUrl(urls, keywords): #choose a good url
	pos, lU, best = 0, len(urls), (None,-1)
	while pos < lU:
		u, t = lU[pos]
		actualScore = makePoint(t, keywords)
		if best[1] < actualScore:
			best = u, actualScore
		pos += 1
	return lU[0][0] #should return best

def openDownloader(url): #to get the url to download
	pass

def downloadFromUrl(url): #actualy download file
	pass

def main(): #get everything work together
	print("Made by Tom Moulard\nAny questions there : tom@moulard.org")
	n = str(input("Any KeyWords ?\n")).split(" ")
	urlQ = urlMaker(n)
	#print(urlQ)
	source = getPageSource(urlQ)
	possibleSources = parsingPage(source)
	#printParsed(possibleSources)
	urlF = chooseUrl(possibleSources, n)
	print(urlF)
main()
