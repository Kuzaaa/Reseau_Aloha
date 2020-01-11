# -*- coding: utf-8 -*-
import random

class Equipement():
    
    def __init__(self, num):
        self.distance = random.randrange(100)
        self.id = num
        
    def affiche(self):
        return "Je suis l'equipement " + str(self.id) + " etant a une distance " + str(self.distance) + "."
    
    #def send(self, equip):

 
print("Combien d'equipement ?")
nb_equip = int(input())
tabEquip = []

for i in range(nb_equip):
    tabEquip.append(Equipement(i+1))
    
print(tabEquip[nb_equip-1].affiche())


