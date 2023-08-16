# projet-2-dignamic

Traitement de données volumineuses et hétérogènes.

## Contexte

Notre client est une **fromagerie** qui possède un datawarehouse depuis 2004 représenté par un fichier .csv, dont le contenu nous a été transmis. 

Il contient des données relatives à un programme de fidélisation : Les clients récupèrent des points à chaque commande puis les dépensent pour obtenir des goodies. 

Chaque individu de notre jeu représente une commande de tels goodies.

Nous avons une problématique volumétrique; et proposerons une solution de stockage des données NoSQL pour que la solution soit pérenne, avec peu de dette technique. Notre choix s'est porté sur Hbase, système de gestion de base de données orientée colonnes, présente dans l'écosystème Hadoop et pré-configuré sur les images dockers qui nous servent de support.

Le jeu de données est disponible à l'adresse suivante : https://diginamic-my.sharepoint.com/personal/cgermain_diginamic_fr/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fcgermain%5Fdiginamic%5Ffr%2FDocuments%2FSessions%2Fdata%5Fsources%2Fdataw%5Ffro03%2Ezip&parent=%2Fpersonal%2Fcgermain%5Fdiginamic%5Ffr%2FDocuments%2FSessions%2Fdata%5Fsources&ga=1

Un NoteBook (pas forcément très lisible ici) a été déposé, contenant tous les travaux d'analyse effectués sous Pandas. Ce travail représente la partie préliminaire de notre projet, nous avons élaboré nos mappers ainsi que nos reducers suite à ce travail exploratoire.

Il y a donc un mapper et un reducer pour chaque problématique (sauf pour le lot 2, où nous n'en avons qu'un de chaque), fonctionnels en local.
Notre interaction avec Hbase (insertion de nos données) a été effectuée avec la librairie Happybase, et disponible dans le fichier .py éponyme !

## Cahier des charges

Le client souhaite obtenir des insights très précis sur son activité dont voici le listing non-exhaustif, trié par lots :

      - Lot1 :
      
            1. Obtenir le nombre de commandes par ville sur le département de la Mayenne (53) regroupé par objet dont la quantité est supérieure à 5 ; par années depuis 2010.

            2. Avoir, pour les 10 clients les plus fidèles depuis 2008 : le nombre, la moyenne et l'écart-type du nombre de colis par ville (avec le département affiché).

            3. Une courbe de croissance par objet selon les départements de la Mayenne (53), de la Sarthe (72) et du Maine et Loir (49).

      Les graphes doivent être transmis au format PDF.


      - Lot2 :

            1. Les 100 meilleures commandes entre 2006 et 2016 avec la ville, le nombre de colis et la somme des "timbrecde".

            2. Tirer 5% du point 1 uniquement sur les départements 53, 61 et 28 ; qui n'ont pas de "timbrecli"; avec la ville, le nombre de colis ainsi que la moyenne des commandes totales. Un graphe de type Camembert est attendu au format PDF.

            3. Exporter les résultats des Lots 1 et 2 sous format Excel.

      - Lot3 :

            Mettre en place une base de données NoSQL por stocker le contenu du fichier .csv et de mettre en oeuvre un moteur de recherche avec ElasticSearch ou Spark pour interroger ce DataWareHouse pour obtenir les résultats des Lots 1 et 2 sans graphe.




