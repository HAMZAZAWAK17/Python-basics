# Gestion des Fichiers en Python
# Ce chapitre explique comment créer, lire et modifier des fichiers texte (.txt)

# 1. Écrire dans un fichier ('w' pour write)
# ATTENTION : 'w' écrase le contenu existant !
with open("exemple.txt", "w", encoding="utf-8") as fichier:
    fichier.write("Bonjour !\n")
    fichier.write("Ceci est une ligne dans mon fichier.\n")
print("Fichier créé et écrit avec succès.")

# 2. Ajouter du contenu ('a' pour append)
with open("exemple.txt", "a", encoding="utf-8") as fichier:
    fichier.write("Ceci est une nouvelle ligne ajoutée à la fin.\n")
print("Contenu ajouté avec succès.")

# 3. Lire un fichier ('r' pour read)
print("\n--- Lecture du contenu du fichier ---")
try:
    with open("exemple.txt", "r", encoding="utf-8") as fichier:
        contenu = fichier.read()
        print(contenu)
except FileNotFoundError:
    print("Erreur : Le fichier n'existe pas.")

# 4. Lire ligne par ligne
print("--- Lecture ligne par ligne ---")
with open("exemple.txt", "r", encoding="utf-8") as fichier:
    for ligne in fichier:
        print(f"Ligne : {ligne.strip()}") # .strip() enlève les sauts de ligne invisibles

# 5. Supprimer le fichier (nécessite le module os)
# import os
# os.remove("exemple.txt")
