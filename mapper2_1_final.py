import sys
#wordList = dict()

first_line = True


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    
    line = line.strip()
    #print(line)
    if first_line:
        first_line = False
        
    
    else:
    
        # split the line into words
        words = line.split(',')
        
        if len(words) != 14: # test pour être sur qu'on ait suffisamment de valeurs dans la liste
            continue
        
        else :
    
            if words[12] in ['2006','2007','2008', '2009','2010','2011', '2012','2013','2014', '2015', '2016']:
            
                print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(words[1], words[3], words[4], words[5], words[6], words[7], words[10], words[11], words[12], words[13]))
                
                # 1 : nomcli
                # 3 : villecli
                # 4 : codcde
                # 5 : timbrecli
                # 6 : timbrecde
                # 7 : Nbcolis
                # 10 : points
                # 11 : Dpt
                # 12: Année
                # 13 : agg_col
                
                

       