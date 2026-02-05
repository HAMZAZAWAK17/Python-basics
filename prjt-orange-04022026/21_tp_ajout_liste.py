# Initialisation d'une liste vide
liste = []

# Demander à l'utilisateur le nombre d'éléments à saisir
nombre = int(input("Combien d'éléments voulez-vous ajouter ? "))

# Boucle pour demander chaque élément
for i in range(nombre):
    # Saisie de l'élément (i+1 pour l'affichage humain)
    element = input(f"Entrez l'élément {i+1} : ")
    # Ajout de l'élément saisi dans la liste
    liste.append(element)

# Affichage du résultat final
print("Voici votre liste finale :")
print(liste)
