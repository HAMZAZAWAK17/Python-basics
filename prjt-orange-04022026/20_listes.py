# Les Listes en Python
# Une liste est une collection ordonnée et modifiable d'éléments.

print("--- 1. Création et Accès ---")
fruits = ["Pomme", "Banane", "Orange", "Kiwi"]
print(f"Ma liste de fruits : {fruits}")

# Accéder aux éléments (l'index commence à 0)
print(f"Le premier fruit (index 0) : {fruits[0]}")
print(f"Le dernier fruit (index -1) : {fruits[-1]}")

print("\n--- 2. Modification ---")
fruits[1] = "Fraise"  # Remplace "Banane" par "Fraise"
print(f"Liste après modification : {fruits}")

print("\n--- 3. Principales Méthodes ---")

# .append() : Ajouter à la fin
fruits.append("Mangue")
print(f"Après append('Mangue') : {fruits}")

# .extend() : Ajouter plusieurs éléments d'une autre liste
autres_fruits = ["Ananas", "Papaye"]
fruits.extend(autres_fruits)
print(f"Après extend(['Ananas', 'Papaye']) : {fruits}")

# .insert() : Ajouter à une position précise
fruits.insert(1, "Cerise") # Insère Cerise à l'index 1
print(f"Après insert(1, 'Cerise') : {fruits}")

# .remove() : Supprimer par valeur
fruits.remove("Orange")
print(f"Après remove('Orange') : {fruits}")

# .pop() : Supprimer par index (et récupérer la valeur)
# Sans index : supprime le dernier
dernier_fruit = fruits.pop() 
print(f"Fruit supprimé (dernier) : {dernier_fruit}")

# Avec index : supprime l'élément à la position donnée
premier_fruit = fruits.pop(0) 
print(f"Fruit supprimé (index 0) : {premier_fruit}")
print(f"Liste restante : {fruits}")

# len() : Longueur de la liste (nombre d'éléments)
nombre_fruits = len(fruits)
print(f"Il reste {nombre_fruits} fruits dans la liste.")

# .count() : Compter le nombre d'occurrences d'un élément
liste_notes = [10, 15, 20, 15, 10, 15]
nombre_quinze = liste_notes.count(15)
print(f"\nListe des notes : {liste_notes}")
print(f"Le nombre 15 apparait {nombre_quinze} fois.")

# .sort() : Trier la liste
nombres = [5, 2, 9, 1, 8]
nombres.sort()
print(f"\nListe de nombres triée : {nombres}")

# .reverse() : Inverser l'ordre
nombres.reverse()
print(f"Liste inversée : {nombres}")

# Vérifier la présence d'un élément
if "Pomme" in fruits:
    print("\nOui, il y a une Pomme dans la liste !")
