# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 08:45:30 2016

@author: moular_b
"""

import random

class Personnage():
    nom = "undefined"
    lp = 20
    force = 2
    def ___inti___(self, nom):
        self.nom = nom
    def fight(self):
        if(random.randint(1,2) % 2 == 0):
            self.lp -= self.force
    def printStat(self):
        print("lp", self.lp, "force", self.force)
    def sayHello(self):
        print("Bonjour", self.nom)

huber = Personnage()
huber.___inti___("hubuer")
huber.fight()
huber.printStat()
huber.sayHello()
