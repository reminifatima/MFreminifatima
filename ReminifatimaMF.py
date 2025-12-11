#REMINI Fatima Zahra,(MF), 11/12/2025
#FEKIH Nafissa 
#HAMED Farah
#YEBDRI Mohammed Nadir

import pandas as pd 

#Données: séquences d'ADN, longueur, pourcentage de GC
data={
  "séquence": ["ATGCGTACGTA","GCTAGCTAGGCC","GCTAGCTAGGCC","TACGATCGTA","ATGAAAGGCTT","CGTACGTAGC","TTAACCGGT"],
  "longueur": [12,12,12,10,11,10,10],
  "pourcentage GC": [50,66.67,58.33,40.45,45,60,50]
  }
#Création du DataFrame (tableau pandas)
df = pd.DataFrame(data)

# *** Prmière partie: Création et affichage ***
print("Analyse des séquence d'ADN")
print(df)
print("\n")

# *** Deuxième partie: Opréations ***
print("******* Opréations *******")

# 1) Sélectionner la colonne "séquence"
sequences = df["séquence"]
print(sequences)
print("\n")


#2) Sélectionner et afficher uniquement la colonne "longueur"
print("************* Affichage de la colonne longueur *************\n")

col_longueur = df["longueur"]
print(col_longueur)
