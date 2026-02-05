# Création d'une liste initiale de fruits
fruits = ["pomme", "banane", "cerise", "orange", "kiwi"]

# Accès aux éléments par index
print(fruits[0])   # Affiche le premier élément
print(fruits[-1])  # Affiche le dernier élément
print(fruits[2])   # Affiche le troisième élément (index 2)

# Modification d'un élément (index 1 est le deuxième)
fruits[1] = "mangue"
print(fruits)

# Ajout d'éléments
fruits.append("ananas")      # Ajoute à la fin de la liste
fruits.insert(0, "fraise")   # Ajoute au début (index 0)
print(fruits)

# Suppression d'éléments
fruits.remove("kiwi")        # Supprime par valeur
fruits.pop()                 # Supprime le dernier élément de la liste
print(fruits)

# Extraction de sous-listes (slicing)
print(fruits[:3])            # Affiche les 3 premiers éléments
print(fruits[-2:])           # Affiche les 2 derniers éléments

# Affichage de la taille de la liste
print(len(fruits))

# Vérification de la présence d'un élément dans la liste
if "banane" in fruits:
    print("Banane est là")

if "peche" in fruits:
    print("Pêche est là")
else:
    print("Pêche n'est pas là")

# Parcourir la liste avec une boucle for
for fruit in fruits:
    print(fruit)
