#!/usr/bin/env python

import sys

first_line = True


# input comes from STDIN (standard input)

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    
    if first_line:
        first_line = False
    else :
    
    # split the line into words

        words = line.split(',')
    
        if int(words[12]) >= 2008 :  # Filtre sur les années --> Cahier des charges
            
            print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(words[0], words[1], words[3], words[7], words[10], words[11], words[12]))

            #print(f"{words[0]}\t{words[1]}\t{words[3]}\t{words[7]}\t{words[10]}\t{words[11]}\t{words[12]}")

            #print('%s\t%s' % (words[0],words[1],words[3],words[10],words[11],words[12]))# affiche cle valeur
# 0 = codcli
# 1 = nomcli
# 3 = villecli
# 7 = Nbcolis
# 10 = points
# 11 = Dpt
# 12 = Année


# --------------->*
