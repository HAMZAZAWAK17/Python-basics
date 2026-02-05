# La boucle FOR (Pour)
# La boucle for est utilisée pour parcourir une séquence (liste, chaîne de caractères, range, etc.)

print("--- 1. Utilisation de range() ---")
# range(start, stop, step)
# Note: 'stop' est exclu. range(5) va de 0 à 4.

print("Compter de 0 à 4 :")
for i in range(5):
    print(i)

print("\nCompter de 1 à 10 :")
for i in range(1, 11):
    print(i)

print("\nCompter de 0 à 20 par pas de 5 :")
for i in range(0, 21, 5):
    print(i)


print("\n--- 2. Parcourir une liste ---")
fruits = ["Pomme", "Banane", "Orange", "Kiwi"]

for fruit in fruits:
    print(f"J'aime manger : {fruit}")


print("\n--- 3. Parcourir une chaîne de caractères ---")
mot = "Python"

print(f"Épeler le mot {mot} :")
for lettre in mot:
    print(lettre)


print("\n--- 4. Exemple Concret : Somme simple ---")
somme = 0
for nombre in range(1, 6): # 1, 2, 3, 4, 5
    somme = somme + nombre
    
print(f"La somme des nombres de 1 à 5 est : {somme}")
