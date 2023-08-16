#!/usr/bin/env python

import sys

first_line = True



for line in sys.stdin:

    
    
    line = line.strip()
    
    if first_line:
        first_line = False
    else :
        words = line.split(',')
    
        if words[11] == '53' or words[11] == '72' or words[11] == '49' :
            print("{}\t{}\t{}\t{}".format(words[8], words[9], words[11], words[12]))

                # 8 = qte
                # 9 = libobj
                # 11 = Dpt
                # 12 = Année