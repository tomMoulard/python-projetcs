#made by moular_b

b32 = ['0','1','2','3','4','5','6','7','8','9','b','c','d','e','f','g', 'h','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z']

#GeoHash2reel
def geoHashToInt(h):
	res =[]
	for x in h:
		for i in range(len(b32)):
			if b32[i] == x :
				res.append(i)
	return res

def intToBitList(n):
	res = []
	for x in range(5):
		res.append(n % 2)
		n //= 2
	return res

def reverseImpaire(l):
	lenL = len(l)
	for x in range(lenL // 2):
		tmp = l[x]
		l[x] = l[lenL - x - 1]
		l[lenL - x - 1] = tmp

def intListToBitList(i):
	res = []
	for x in i:
		l = intToBitList(x)
		reverseImpaire(l)
		for y in l:
			res.append(y)
	return res

def separate(l):
	lat, longi, pos, ll = [], [], 0, len(l)
	while pos < ll:
		if pos % 2 == 0:
			longi.append(l[pos])
		else:
			lat.append(l[pos])
		pos += 1
	return (longi, lat)

def bListToReel(l, bSup):
	bInf, mid = -bSup, 0
	for x in range(len(l)):
		if l[x] == 1:
			bInf = mid
			mid = (mid + bSup) / 2
		else:
			bSup = mid
			mid = (mid + bInf) / 2
	return mid

def main():
	h = str(input("hash ?"))
	longi, lat = separate(intListToBitList(geoHashToInt(h)))
	print("longitude", longi, "\nLatitude", lat, "\nReal Longitude", bListToReel(longi, 180), "\nReal Latitude", bListToReel(lat, 90))

#main()

#reels2GeoHash
def reelToBitList(pos, delta):
	resL = []
	res = pos
	
