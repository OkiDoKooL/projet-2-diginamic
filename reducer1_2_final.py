import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# 0 = codcli
# 1 = nomcli
# 2 = villecli
# 3 = Nbcolis
# 4 = points
# 5 = Dpt
# 6 = Année


columns_22 = ['codcli', 'nomcli', 'villecli', 'Nbcolis', 'points', 'Dpt', 'Année']
data = []
liste_traitement = ['codcli', 'Nbcolis', 'points', 'Dpt', 'Année']

#Lecture de la donnée qui se trouve dans l'input standard

for line in sys.stdin:
    
    data_line = line.strip().split('\t')
    print(data_line)
    if len(data_line) != 7:
        continue
        
    data.append(data_line)

# Transformation de la liste data (qui contient autant de liste qu'il y a de données lues) en un pd.DataFrame

df = pd.DataFrame(data, columns = columns_22)

# Boucle de traitement des types, conersion des strings en int

for col in liste_traitement :
    
    if col == 'points':
        df[col] = df[col].astype(float)
    else :
    
        df[col] = df[col].astype(int)

    


df_2_group = df.groupby(["codcli"]).agg(
    {
        "points": "sum",
        "Nbcolis": "sum",
        "villecli": "first",
        "Dpt": "first",
        "nomcli": "first",
    }
)


df_2_group_top10 = df_2_group.sort_values("points", ascending=False).head(10) 


df_2_group_top10_by_ville = df_2_group_top10.groupby(["villecli"]).agg({"Nbcolis":["sum","mean","std"]}) # Caclul sur NbColis par ville



df_2_group_top10_by_ville_tri_sum = df_2_group_top10_by_ville.sort_values(('Nbcolis','sum'), ascending = False)

df_2_group_top10_by_ville_tri_mean = df_2_group_top10_by_ville.sort_values(('Nbcolis','mean'), ascending = False)

df_2_group_top10_by_ville_tri_std = df_2_group_top10_by_ville.sort_values(('Nbcolis','std'), ascending = False)


# Graphe 1 : Somme des Nbcolis par ville pour les 10 clients les plus fidèles



plt.figure()  # Créer une nouvelle figure pour chaque graphe
plt.bar(df_2_group_top10_by_ville_tri_sum.index, df_2_group_top10_by_ville_tri_sum[('Nbcolis',  'sum')])
plt.xlabel("villecli")
plt.ylabel(('Nbcolis',  'sum'))
plt.title(f"{('Nbcolis',  'sum')} par ville")
plt.xticks(rotation=90)  # Faire pivoter les étiquettes des villes pour une meilleure lisibilité
plt.savefig('fidelite_1_sum.pdf')
plt.show()


# Graphe 2 : Moyenne des Nbcolis par ville pour les 10 clients les plus fidèles

plt.figure()  
plt.bar(df_2_group_top10_by_ville_tri_mean.index, df_2_group_top10_by_ville_tri_mean[('Nbcolis',  'mean')])
plt.xlabel("villecli")
plt.ylabel(('Nbcolis',  'mean'))
plt.title(f"{('Nbcolis',  'mean')} par ville")
plt.xticks(rotation=90)  # Faire pivoter les étiquettes des villes pour une meilleure lisibilité
plt.savefig('fidelite_2_mean.pdf')
plt.show()





# Graphe 3 : Ecart-type du Nbcolis par ville pour les 10 clients les plus fidèles

plt.figure()  
plt.bar(df_2_group_top10_by_ville_tri_std.index, df_2_group_top10_by_ville_tri_std[('Nbcolis',  'std')])
plt.xlabel("villecli")
plt.ylabel(('Nbcolis',  'std'))
plt.title(f"{('Nbcolis',  'std')} par ville")
plt.xticks(rotation=90)  # Faire pivoter les étiquettes des villes pour une meilleure lisibilité
plt.savefig('fidelite_3_std.pdf')
plt.show()







    # Envoi dans stdout des lignes de mon dataframe sous la forme de tuples contenant toutes les valeurs sous la forme de strings
    
#for index, row in df_2_lot_12_group_top10_by_ville_tri_sum.iterrows():
 #       tuple_filtre = tuple(row)
  #      print(tuple_filtre)
    
    



























































