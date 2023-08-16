import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

                # 0 : nomcli
                # 1 : villecli
                # 2 : codcde
                # 3 : timbrecli
                # 4 : timbrecde
                # 5 : Nbcolis
                # 6 : points
                # 7 : Dpt
                # 8: Année
                # 9 : agg_col


columns_21 = ['nomcli', 'villecli', 'codcde', 'timbrecli', 'timbrecde', 'Nbcolis','points', 'Dpt', 'Année','agg_col']
data = []
liste_traitement = ['codcde', 'timbrecli', 'timbrecde', 'Nbcolis', 'points', 'Dpt', 'Année', 'agg_col']

for line in sys.stdin:
    
    data_line = line.strip().split('\t')
    print(data_line)
    if len(data_line) != 10:
        continue
        
    data.append(data_line)

# Transformation de la liste data (qui contient autant de liste qu'il y a de données lues) en un pd.DataFrame

df = pd.DataFrame(data, columns = columns_21)

for col in liste_traitement :
    
    if col in ['timbrecli', 'timbrecde', 'points']:
        df[col] = df[col].astype(float)
    else :
    
        df[col] = df[col].astype(int)



# Aggrégat sur la variable 'codcde' pour bien identifier les 100 meilleures commandes et ce que
# l'on souhaite regarder dessus
df_group = df.groupby(["codcde"]).agg(
    {
        "nomcli": 'first',
        "Dpt": "first",
        "villecli": "first",
        "timbrecli": "sum",
        "timbrecde": "sum",
        "Nbcolis": "sum",
        "points": "sum",
        "agg_col": "sum",
    }
)


# On renomme la dernière colonne de notre nouveau DataFrame qui correspond à la quantité de commandes

df_group.rename(columns={'agg_col': 'qte_objets_commandes'}, inplace=True)


#Tri de notre jeu par valeurs de points décroissante pour obtenir le top100 des commandes 

df_group_tri = df_group.sort_values('points', ascending = False).head(100)

print(df_group_tri.head(20))

df_group_tri.to_excel("reponse_21.xlsx", index = False, header = True)


# On effectue un filtre du jeu de sortie de la Q1 sur les départements et sur 'timbrecli'

df_22 = df_group_tri.query('Dpt == 28 or Dpt == 61 or Dpt == 53')

# Nouveau filtre sur la variable 'timbrecli' qui se doit de valoir 0 ou d'être NaN
df_22 = df_22.loc[
    (df_22["timbrecli"].isnull() == True) | (df_22["timbrecli"] == 0)
]

print(df_22.shape)

# Tirage de 5 % de notre jeu des meilleures commandes filtrées par département
df_22_tirage = df_22.sample(frac = 0.05, random_state=10)

qte_objets_commande_totale = df_22_tirage['qte_objets_commandes'].sum()

df_22_tirage['proportion_objets_commandés'] = df_22_tirage['qte_objets_commandes']/qte_objets_commande_totale

print(df_22_tirage)

#Exportation des résultats sous excel

df_22_tirage.to_excel('reponse_lot_22.xlsx', index = False, header = True)

# Créer le diagramme en camembert
plt.figure(figsize=(10, 6))
plt.pie(df_22_tirage['proportion_objets_commandés'], labels=df_22_tirage['nomcli'], autopct='%1.1f%%', startangle=140)
plt.title('Proportion d\'objets commandés par commande')
plt.axis('equal')  
plt.savefig('graphe_22_camembert.pdf')
plt.show()































