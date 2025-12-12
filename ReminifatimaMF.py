#REMINI Fatima Zahra,(MF), 11/12/2025
#FEKIH Nafissa 
#HAMED Farah
#YEBDRI Mohammed Nadir

import pandas as pd 

#Données: Séquences ADN, Longueur, Pourcentage de GC
data={
  "Séquence": ["ATGCGTACGTA","GCTAGCTAGGCC","GCTAGCTAGGCC","TACGATCGTA","ATGAAAGGCTT","CGTACGTAGC","TTAACCGGAT"],
  "Longueur": [12,12,12,10,11,10,10],
  "Pourcentage GC": [50,66.67,58.33,40,45.45,60,50]
  }
#Création du DataFrame (tableau pandas)
df = pd.DataFrame(data)

# *** Première partie: Création et affichage ***
print("Analyse des Séquences ADN")
print(df)
print("\n")

# *** Deuxième partie: Opérations ***
print("******* Opérations *******")

# 1) Sélectionner la colonne "Séquence"
sequences = df["Séquence"]
print(sequences)
print("\n")

#2) Sélectionner et afficher uniquement la colonne "Longueur"
print("************* Affichage de la colonne Longueur *************\n")

col_longueur = df["Longueur"]
print(col_longueur)

#3) Filtrer les séquences avec la Longueur est supérieur à 10
print("*********** Filtrage: Longueur supérieur à 10 ***********") 
#Filtrer les séquences avec la Longueur est supérieur à 10
filtered_df=df[df["Longueur"]>10]
print(filtered_df)

#4) Calculer la moyenne du pourcentage de GC après la virgule 
print("*********** Calcul de la moyenne ***********")
#Calculer la moyenne du pourcentage de GC Avec 3 chiffres après la virgule
average_gc = df["Pourcentage GC"].mean()
print(f"Pourcentage moyen de GC:{average_gc:.3f}%")

#5) Ajouter une nouvelle colonne "Catégorie GC"
print("************* Ajouter une nouvelle colonne 'Catégorie GC' *************")
#Ajouter une nouvelle colonne "Catégorie GC"
df["Catégorie GC"] = df["Pourcentage GC"].apply(lambda x: "Riche" if x > 55 else ("Moyen" if 45 <= x <= 55 else "Faible"))
print(df)
#6) Ajouter colonne du nombre de 'G'
df["Nb_G"] = df["Séquence"].apply(lambda seq:seq.count("G"))
print(df)

#7 Calculer l'écart-type du %GC de la Longueur
ecart_gc= df["Pourcentage GC"].std()
ecart_Longueur=df["Longueur"].std()
print("\nÉcart-type%GC:",ecart_gc)
print("Écart-type Longueur:",ecart_longueur)

#8) Sauvegarder le tableau final dans un fichier CSV 
#sauvegarder le tableau final dans un fichier CSV 
df.to_csv("tableau_sequenses.csv",index=false)
print("Fichier CSV sauvgardé avec succés")
