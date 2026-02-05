# 1. Création de la liste
fruits = ["pomme", "banane", "cerise", "orange", "kiwi"]

# 2. Accéder aux éléments
print(fruits[0])   # Premier
print(fruits[-1])  # Dernier
print(fruits[2])   # Troisième

# 3. Modifier des éléments
fruits[1] = "mangue"
print(fruits)

# 4. Ajouter des éléments
fruits.append("ananas")      # À la fin
fruits.insert(0, "fraise")   # Au début
print(fruits)

# 5. Supprimer des éléments
fruits.remove("kiwi")
fruits.pop()                 # Enlève le dernier
print(fruits)

# 6. Afficher une partie
print(fruits[:3])  # Les 3 premiers
print(fruits[-2:]) # Les 2 derniers

# 7. Longueur
print(len(fruits))

# 8. Recherche
if "banane" in fruits:
    print("Banane est là")

if "peche" in fruits:
    print("Pêche est là")
else:
    print("Pêche n'est pas là")

# 9. Boucle for
for fruit in fruits:
    print(fruit)
