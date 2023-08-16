
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 0 = qte
# 1 = libobj
# 2 = Dpt
# 3 = Année

columns_13 = ['qte', 'libobj', 'Dpt', 'Année']
data = []
liste_traitement = ['Dpt', 'Année', 'qte']


for line in sys.stdin:
    
    data_line = line.strip().split('\t')
    print(data_line)
    if len(data_line) != 4:
        continue
        
    data.append(data_line)

# Transformation de la liste data (qui contient autant de liste qu'il y a de données lues) en un pd.DataFrame

df = pd.DataFrame(data, columns = columns_13)

# Conversion des types de chaque colonne

for col in liste_traitement :
    
    df[col] = df[col].astype(int)

# Aggrégat sur ce qui nous intéresse

df_group = df.groupby(['libobj','Dpt','Année']).agg({"qte": 'sum'})


print(df_group)

#### Fonction pour afficher l'évolution du nombre d'objet commandé par année et Dpt


def graph_courbe_croissance(name, df, path = None) :
    '''Fonction qui renvoie l\'évolution du nombre d\'objets commandés par années et par Dpt '''
    df = df.reset_index()
    selected_libobj = name  # Définit l'objet à sélectionner
    selected_libobj_data = df.loc[df['libobj'] == selected_libobj]

    # Création du graphique pour le libobj
    fig, ax = plt.subplots()

    # Boucler à travers les valeurs de Dpt unique pour l'objet sélectionner
    for dpt, group_data in selected_libobj_data.groupby('Dpt'):
        qte_values = group_data['qte']
        années = group_data['Année']
        label = f"Dpt: {dpt}"
        ax.plot(années, qte_values, marker='o', label=label)

    ax.set_xlabel('Année')
    ax.set_ylabel('Quantité vendue (qte)')
    ax.set_title(f"Quantité vendue pour '{selected_libobj}' par Année et Dpt")
    ax.legend()

    # Afficher le graph
    plt.tight_layout()
    
    if path is not None :
        plt.savefig(path)   # Enregistre le graphique dans le chemin stipulé
    plt.show()
    
graph_courbe_croissance("Montre", df_group, r'C:\Users\Alexandre\graphe_test_zizi.pdf')
graph_courbe_croissance("Drap de bain", df_group)
graph_courbe_croissance("Stylo plume", df_group)
graph_courbe_croissance("Pin's", df_group)