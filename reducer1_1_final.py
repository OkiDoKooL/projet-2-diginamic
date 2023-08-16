from operator import itemgetter
import sys
# 0 = villecli
# 1 = qte
# 2 = libobj
# 3 = Dpt
# 4 = Année

current_villeclient = None
current_objet = None
objet = None
villeclient = None
quantite = 0
compteur = 0
current_compteur = 0
dpt = None
annee = None


# input comes from STDIN
for line in sys.stdin:
    
    # Retrait des espaces en début et fin de ligne
    line = line.strip()
   
    if len(line.split(',')) != 6:
           continue
    # Parseur de ligne
    words = line.split(',')
    
    
    dpt, villeclient, objet,  quantite, annee, compteur = words[0], words[1], words[2], words[3], words[4], words[5]
    
    
    
    
    
    
    
    try:
        compteur = int(compteur)
        
    except ValueError:
            # Vérification sur le compteur pour être sur que l'on ait bien un nombre entier
            
            continue
    # Aggregat sur villeclient et objet
    
    if current_villeclient == villeclient and current_objet == objet:
        
        current_compteur += compteur  # Compteur de commandes
    
    else :
    
        if current_villeclient == villeclient and current_objet:
            print("{}\t{}\t{}\t{}\t{}".format(dpt, current_villeclient, current_objet, current_compteur, annee))

            #print(f"{dpt}\t{current_villeclient}\t{current_objet}\t{current_compteur}\t{annee}")  #print cle valeur
            current_objet = objet
            current_compteur = compteur
        else :
            if current_villeclient and current_objet:
                
                # Ecriture des résultats dans stdout
                print("{}\t{}\t{}\t{}\t{}".format(dpt, current_villeclient, current_objet, current_compteur, annee))

                #print(f"{dpt}\t{current_villeclient}\t{current_objet}\t{current_compteur}\t{annee}") #print cle valeur
            current_villeclient = villeclient   #passer à la cle suivante
            current_objet = objet
            current_compteur = compteur  #initialisation du compteur de la ville suivante
    print("------------------------------------------------")
       
if current_villeclient == villeclient and current_objet == objet:
    print("{}\t{}\t{}\t{}\t{}".format(dpt, current_villeclient, current_objet, current_compteur, annee))

    #print(f"{dpt}\t{current_villeclient}\t{current_objet}\t{current_compteur}\t{annee}")
