#!/usr/bin/env python

import sys


premiere_ligne = True
compteur = 1

# Ici c'est du streaming
for line in sys.stdin:
    
    
    line = line.strip()     # Retire les espaces en début et fin de string
    
    if premiere_ligne:
        premiere_ligne = False
        continue                                     # Ignorer la première ligne
    
    else:
    
        # split the line into words
        words = line.split(',')
    
        if len(words) < 13: # test pour être sr que l'on ait suffisamment de valeurs dans la liste
            continue
        if int(words[11]) == 53 :
            if int(words[8]) >= 5 :
                if int(words[12]) >= 2010 :
                    #print(f"{words[11]},{words[3]},{words[9]},{words[8]},{words[12]},{compteur}") sur p3.6+
                    print("{},{},{},{},{},{}".format(words[11], words[3], words[9], words[8], words[12], compteur))
                # 11 = Dpt
                # 3 = villecli
                # 9 = libobj
                # 8 = qte
                # 12 = Année



