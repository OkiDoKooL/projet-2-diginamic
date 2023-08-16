# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:32:10 2023

@author: massi
"""
import happybase
import pandas as pd
from datetime import datetime

path = r'C:\lot2Q1\reponse_21.xlsx'
df21 = pd.read_excel(path)

connection = happybase.Connection('localhost', 9090)

connection.create_table(
    'Lot3',
    {'cf21': dict(max_versions=10),
     'cf22': dict(max_versions=10)
     }
)

table = connection.table('Lot3')

#### Les 100 meilleures commandes
for index, row in df21.iterrows() :
        row_key = datetime.now().strftime("%H:%M:%S.%f") 
        #print(row_key)# Utiliser l'index de la ligne comme clé
        table.put(str(row_key), {
            b'cf21:nomcli': str(row['nomcli']).encode(),
            b'cf21:Dpt': str(row['Dpt']).encode(),
            b'cf21:villecli': str(row['villecli']).encode(),
            b'cf21:timbrecli': str(row['timbrecli']).encode(),
            b'cf21:timbrecde': str(row['timbrecde']).encode(),
            b'cf21:Nbcolis': str(row['Nbcolis']).encode(),
            b'cf21:points': str(row['points']).encode(),
            b'cf21:qte_objets_commandes': str(row['qte_objets_commandes']).encode()
        })


#able.put('8',{
             #           b'cf21:nomcli': b'mary',
                 #      b'cf21:Dpt': b'61'})



path = r'C:\lot2Q1\reponse_lot_22.xlsx'
df22 = pd.read_excel(path)
print(df22)

connection = happybase.Connection('localhost', 9090)


table = connection.table('Lot3')

#### Tirage 5% des 100 meilleures commandes           
for index, row in df22.iterrows() :
        row_key = datetime.now().strftime("%H:%M:%S.%f") 
        print(row_key)# Utiliser l'index de la ligne comme clé
        table.put(str(row_key), {
            b'cf22:nomcli': str(row['nomcli']).encode(),
            b'cf22:Dpt': str(row['Dpt']).encode(),
            b'cf22:villecli': str(row['villecli']).encode(),
            b'cf22:timbrecli': str(row['timbrecli']).encode(),
            b'cf22:timbrecde': str(row['timbrecde']).encode(),
            b'cf22:Nbcolis': str(row['Nbcolis']).encode(),
            b'cf22:points': str(row['points']).encode(),
            b'cf22:qte_objets_commandes': str(row['qte_objets_commandes']).encode()
            #b'cf22:proportion_objets_commandes': str(row['proportion_objets_commandes']).encode()
            
        })
        
        
connection.create_table(
    'Lot4',
    {'cf21': dict(),
     'cf22': dict()
     }
)
