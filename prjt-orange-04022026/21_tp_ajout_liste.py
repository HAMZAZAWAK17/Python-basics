liste = []
nombre = int(input("Combien d'éléments voulez-vous ajouter ? "))

for i in range(nombre):
    element = input(f"Entrez l'élément {i+1} : ")
    liste.append(element)

print("Voici votre liste finale :")
print(liste)
