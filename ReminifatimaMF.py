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

#3) filtrer les séquences avec la Longueur est supérieurr a 10%
print("*********** Filtrage Avec pourcentage % ***********") 
#Filtrer les séquences avec la Longueur est supérieur à 10
filtered_df=df[df["Longueur"]>10]
print(filtered_df)

#4) calculer la moyenne du pourcentage de GC aprés la virgule 
print("*********** Calcul de la moyenne ***********")
#Calculer la moyenne du pourcentage de GC Avec 3 chifrre aprés la virgule
average_gc = df["Pourcentage GC"].mean()
print(f"Pourcentage moyen de GC:{average_gc:.3f}%")

#5) Ajouter une nouvelle colonne "Catégorie GC
print("************* Ajouter une nouvelle colonne catégorie GC*************")
#Ajouter une nouvelle colonne"catégorie GC"
df["Catégorie GC"] = df["Pourcentage GC"].apply(lamba x: "Riche" if x > 55)
print(df)
