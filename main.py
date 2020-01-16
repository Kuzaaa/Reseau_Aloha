# -*- coding: utf-8 -*-

###############################################################################
#                                    IMPORT                                   #
###############################################################################

import random
import math

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
            
        self.T = (50*self.sf_min)/125000
        
    def affiche(self):
        return ("Je suis l'equipement " + str(self.id) + 
                " etant a une distance " + str(self.distance) + 
                " et ayant acces au sf " + str(self.sf_min) + 
                " donnant un temps d'envoie de message de " + str(self.T) +".")
        
    def get_sf(self):
        return self.sf_min
    
    def proba_coll(self):
        self.P = 1 - (math.exp(-2 * (1/240) * dict_sf[self.sf_min] * self.T))
    
    def send(self, equip):
        if(self.sf_min == -1):
            pass
        global dict_coll
        if(self.sf_min == equip.sf_min):
            test = random.uniform(0, 1)
            while(test < self.P):
                #print("collision")
                dict_coll[self.sf_min] += 1
                test = random.uniform(0, 1)

###############################################################################
#                                     MAIN                                    #
###############################################################################

dict_coll = {}
dict_coll[-1] = 0
dict_coll[7] = 0
dict_coll[8] = 0
dict_coll[9] = 0
dict_coll[10] = 0
dict_coll[11] = 0
dict_coll[12] = 0

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
        
#On demande le nombre d'envoi a effectuer
ok = 0 #false -> not ok
while(not(ok)):
    print("Combien d'envoi ?")
    nb_send = input()
    
    try:
        nb_send = int(nb_send)
        if(nb_send >= 1):
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
#print(tabEquip[nb_equip-1].affiche())

dict_sf = {}
dict_sf[-1] = 0
dict_sf[7] = 0
dict_sf[8] = 0
dict_sf[9] = 0
dict_sf[10] = 0
dict_sf[11] = 0
dict_sf[12] = 0

for i in range(len(tabEquip)):
    dict_sf[tabEquip[i].get_sf()] += 1
    
#print(dict_sf)

for i in range(len(tabEquip)):
    tabEquip[i].proba_coll()

for i in range(nb_send):
    #print(i)
    tabEquip[random.randrange(nb_equip)].send(tabEquip[random.randrange(nb_equip)])
    
print(dict_coll)

nb_coll = 0
for coll in dict_coll.values():
    nb_coll += coll

print("Taux de paquets reçus = ",nb_send/(nb_send + nb_coll))