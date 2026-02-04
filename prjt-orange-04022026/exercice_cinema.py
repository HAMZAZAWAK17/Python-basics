# Exercice : Système de gestion des tickets de cinéma

# 1. Demander l'âge
age = int(input("Entrez votre âge : "))

# 2. Demander si la personne a une carte d'étudiant
carte = input("Avez-vous une carte d'étudiant (oui/non) ? ")

# 3. Demander l'horaire de la séance
horaire = input("Entrez l'horaire (matin, apres-midi, soir) : ")

# Initialisation du prix
prix = 0

# Logique de calcul du prix
if age < 12:
    prix = 50

elif age >= 12 and age <= 17:
    if carte == "oui":
        prix = 50
    else:
        prix = 70

else: # Pour les 18 ans et plus
    # Prix de base selon l'horaire
    if horaire == "soir":
        prix = 120
    else: # matin ou apres-midi
        prix = 100
    
    # Application de la réduction étudiant (20 DH)
    if carte == "oui":
        prix = prix - 20

# Affichage du résultat
print("Le prix de votre ticket est de :", prix, "DH")
