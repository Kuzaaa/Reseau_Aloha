# -*- coding: utf-8 -*-

###############################################################################
#                                    IMPORT                                   #
###############################################################################

import random

###############################################################################
#                                CLASS EQUIPEMENT                             #
###############################################################################

class Equipement():
    
    def __init__(self, num, dist_max):
        self.distance = random.randrange(dist_max)
        self.id = num
        ratio = self.distance / dist_max
        if(ratio < 0.4):
            self.sf_min = 7
        elif(ratio < 0.5):
            self.sf_min = 8
        elif(ratio < 0.6):
            self.sf_min = 9
        elif(ratio < 0.7):
            self.sf_min = 10
        elif(ratio < 0.8):
            self.sf_min = 11
        elif(ratio < 0.9):
            self.sf_min = 12
        else:
            self.sf_min = -1
        
    def affiche(self):
        return "Je suis l'equipement " + str(self.id) + " etant a une distance " + str(self.distance) + " et ayant acces au sf " + str(self.sf_min) + "."
    
    #def send(self, equip):

###############################################################################
#                                     MAIN                                    #
###############################################################################

#On demande le nombre d'equipement
ok = 0 #false -> not ok
while(not(ok)):
    print("Combien d'equipement ?")
    nb_equip = input()
    
    try:
        nb_equip = int(nb_equip)
        if(nb_equip >= 1):
            ok = 1
        else:
            print("Veuillez entrer un nombre superieur a 0 :")
    except:
        print("Veuillez entrer un nombre :")
    
#On demande la distance maximum de repartition des equipements
ok = 0 #false -> not ok
while(not(ok)):
    print("Distance maximum ?")
    dist_max = input()
    
    try:
        dist_max = int(dist_max)
        if(dist_max >= 1):
            ok = 1
        else:
            print("Veuillez entrer un nombre superieur a 0 :")
    except:
        print("Veuillez entrer un nombre :")

#Tableau des equipements
tabEquip = []

#Instanciation des equipements
for i in range(nb_equip):
    tabEquip.append(Equipement(i+1, dist_max))
    
#Print de test du dernier equipement cree
print(tabEquip[nb_equip-1].affiche())


