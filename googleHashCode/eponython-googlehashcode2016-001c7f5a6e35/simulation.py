#import parse.py
from math import sqrt

# parse the file
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
			s += str(self.id) + " "
			s += str(self.item.id) + " " + str(self.item.number)
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
		self.addPath(Path(postart, posend))

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

