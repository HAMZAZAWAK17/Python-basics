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

# .insert() : Ajouter à une position précise
fruits.insert(1, "Cerise") # Insère Cerise à l'index 1
print(f"Après insert(1, 'Cerise') : {fruits}")

# .remove() : Supprimer par valeur
fruits.remove("Orange")
print(f"Après remove('Orange') : {fruits}")

# .pop() : Supprimer par index (et récupérer la valeur)
fruit_supprime = fruits.pop() # Supprime le dernier si pas d'index précisé
print(f"Fruit supprimé avec pop() : {fruit_supprime}")
print(f"Liste restante : {fruits}")

# len() : Longueur de la liste (nombre d'éléments)
nombre_fruits = len(fruits)
print(f"Il reste {nombre_fruits} fruits dans la liste.")

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
