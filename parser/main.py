#made by tomMoulard


#parse
def parseList(l):
	res = ""
	for w in l:
		res += w
	return res


#out

#main
def main():
	#print("Made by Tom Moulard\nAny question ? -> Ask there : tom@moulard.org")
	s = input("file to parse ?\n")
	t = open(s)
	n = t.read().split("\n")
	t.close
	for x in n:
		print(x)
	res = parseList(n)
	print(res)
	file = open(s + "_parsed", "w")
	file.write(res)
	file.close

main()
