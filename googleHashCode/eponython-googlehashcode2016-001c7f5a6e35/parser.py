from math import sqrt

class Parameters:
    def __init__(self,file):
        self.file = open(file).readlines()
        self.readSimu(self.file)
        self.readProd(self.file)
        self.readWareHouses(self.file)
        self.readOrders(self.file)
        
        
    def readSimu(self,l):
        
        lst = ["", "", "", "", ""]
        i = 0
        for e in l[0]:
            if e == ' ' or e == '\n':
                i += 1
            else :
                lst[i] += e
        i = 0
        for e in lst:
            lst[i] = int(e)
            i += 1
        self.rows = lst[0]
        self.col = lst[1]
        self.drones = lst[2]
        self.turns = lst[3]
        self.weigh = lst[4]
        
        
    def readProd(self,f):
        nb, weighs = int(f[1]) , f[2].split(' ')     
        i = 0   
        for e in weighs:
            weighs[i] = int(e)
            i += 1
        self.productNb = nb
        self.weighs = weighs
        
    def readWareHouses(self,f):
        self.wareHousesNb = int(f[3])
        self.wareHouses = []
        i = 0 
        while i < self.wareHousesNb:
            l = f[4 + 2 * i].split(' ')
            x, y = int(l[0]) , int(l[1])
            
            inv = []
            l = f[5 + 2 * i].split(' ')
            for e in l:
                inv.append(int(e))
            ware = [x ,y ,inv]
            self.wareHouses.append(ware)
            i += 1
            
    def readOrders(self,f):
        index = self.wareHousesNb * 2 + 4 
        self.orderNb = int(f[index])
        self.orders = []
        index += 1
        i = 0
        length = len(f) - 3
        while index < length and i < self.orderNb:
            l = f[index].split(' ')
            x ,y = int(l[0]) , int(l[1])
            index += 1
            nb = int(f[index])
            index += 1
            prod = []
            l = f[index].split(' ')
            for p in l:
                prod.append(int(p))
            self.orders.append([x,y,prod])
            index += 1

        
#p = Parameters("busy_day.in")
#print(p.rows)
#print(p.col)
#print(p.drones)
#print(p.turns)
#print(p.mxWeigh)
#print(p.productNb)
#for i in p.weighs:
#    print(i, end = " ")
#for i in p.wareHouses:
#    print(i)
#import parse.py

class Item:
	
	def __init__(self, _id, _weigth, _number=1):
		self.id = _id
		self.number = _number
		self.weigth = _weigth

class Instruction:
	
	def __init__(self, _name, _id=0, _item=0, _pos=0, _turn=0):
		self.name = _name
		if _name != "W":	
			self.item = _item
			self.pos = _pos
			self.id = _id
		self.turn = _turn

	def __str__(self):
		s += self.name + " "
		if self.name == "W":
			s += str(self.turn)
		else :
			s += str(self.pos) + " "
			s += str(self.item.pos) + " " + str(self.item.number)
		return s
	
class Drone:
	
	def __init__(self, _id, _comtag, _idwarh, _weigthmax, _pos):
		self.id = _id
		self.comtag = _comtag
		self.idwarh = _idwarh
		self.lofitem = []
		self.lofinstruct = []
		self.nofinstruct = 0
		self.weigth = 0
		self.weigthmax = _weigthmax
		self.pos = _pos

	def addItem(self, item):
		self.lofitem.append(item)
		self.weigth += item.weigth * item.number

	def removeItem(self, _item, n):
		i = 0
		removed = False
		l = len(self.lofitem)
		while i < l and not remove:
			item = self.lofitem[i]
			if item.id == _item.id:
				if n > item.number:
					raise Exception("Not possible to delete this number of item")
				elif n == item.number:
					self.lofitem.remove(item)
				else:
					item.number -= n
					self.lofitem[i] = item
				self.weigth -= (n * item.weigth)
				removed = True

	def addInstruction(self, instruct):
		self.lofinstruct.append(instruct)
		self.nofinstruct += 1

	def removeInstruction(self, instruct):
		self.lofinstruct.remove(instruct)
		self.nofinstruct -= 1

	def Load(self, item, postart, posend):
		if self.weigth + (item.weigth * item.number) > self.weigthmax:
			raise Exception("Not possible to load this items")
		self.addInstruction(Instruction("L", item, posend))

	def Unload(self, item, postart, posend):
		self.addInstruction(Instruction("U", item, posend))

	def Deliver(self, item, postart, posend):
		self.addInstruction(Instruction("D", item, posend))

	def Wait(self, turn):
		self.addInstruction(Instruction("W", turn))

	def executeInstruct(self):
		l = []
		for instruct in self.lofinstruct:
			l.append(str(self.id) + " " + str(instruct))
		return l

class Path:

	def __init__(self, _start, _end):
		self.start = _start
		self.end = _end
		self.cost = (sqrt(abs(self.start.x - self.end.x)**2
			+ abs(self.start.y - self.end.y)**2))

	def __str__(self):
		return(str(self.start) + " -> " + str(self.end) + " cost : "
			+ str(self.cost))
			
			
def getClosestHouse(x,y,lst,id,nb):
    lst = getListOfContainers(lst,id,nb)
    d = ((lst[0][0][0] + x)**2 + (lst[0][0][1] + y)**2)
    iH = lst[0][1]
    i = 0
    l = len(lst)
    while i < l:
        e = lst[i][0]
        tmp = ((e[0] + y)**2 + (e[1] + y)**2)
        if tmp < d:
            iH = lst[i][1]
        i += 1
    return iH


def getListOfContainers(lst,id,nb):
    l = []
    for h in lst:
        le = len(h[2])
        i = 0
        found = False
        while i < le and not found:
            if h[2][id] >= nb:
                found = True
            i += 1
        if found : l.append([h,i])
    return l
