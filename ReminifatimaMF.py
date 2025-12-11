#REMINI Fatima Zahra,(MF), 11/12/2025
#FEKIH Nafissa 
#HAMED Farah
#YEBDRI Mohammed Nadir

import pandas as pd 

#Données: Séquences ADN, Longueur, Pourcentage de GC
data={
  "Séquence": ["ATGCGTACGTA","GCTAGCTAGGCC","GCTAGCTAGGCC","TACGATCGTA","ATGAAAGGCTT","CGTACGTAGC","TTAACCGGT"],
  "Longueur": [12,12,12,10,11,10,10],
  "Pourcentage GC": [50,66.67,58.33,40.45,45,60,50]
  }
#Création du DataFrame (tableau pandas)
df = pd.DataFrame(data)

# *** Prmière partie: Création et affichage ***
print("Analyse des Séquence ADN")
print(df)
print("\n")

# *** Deuxième partie: Opréations ***
print("******* Opréations *******")

# 1) Sélectionner la colonne "Séquence"
sequences = df["Séquence"]
print(sequences)
print("\n")


#2) Sélectionner et afficher uniquement la colonne "Longueur"
print("************* Affichage de la colonne Longueur *************\n")

col_longueur = df["Longueur"]
print(col_longueur)
