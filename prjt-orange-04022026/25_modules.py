# Les Modules en Python
# Un module est un fichier contenant du code Python (fonctions, variables) 
# que l'on peut réutiliser dans d'autres programmes.

# 1. Importer un module complet (Standard)
import math
print(f"La racine carrée de 16 est : {math.sqrt(16)}")
print(f"La valeur de Pi est : {math.pi}")

# 2. Importer une fonction spécifique d'un module
from random import randint
nombre_aleatoire = randint(1, 100)
print(f"Nombre aléatoire entre 1 et 100 : {nombre_aleatoire}")

# 3. Utiliser un alias (renommer le module)
import datetime as dt
maintenant = dt.datetime.now()
print(f"Date et heure actuelle : {maintenant}")

# 4. Importer tout d'un module (Déconseillé mais possible)
# from os import * 

print("\n--- Pourquoi utiliser des modules ? ---")
print("- Gain de temps (code déjà prêt)")
print("- Organisation du code (séparation par thèmes)")
print("- Accès à des fonctionnalités puissantes (calculs, fichiers, web)")
