#basics:
#boucle infinie: bonjour s'affiche infiniment (sans arret)
i=0
while i<10:
    print("bonjour")
############################
#boucle correcte: bonjour s'affiche 10 fois
i=0
while i<10:
    print("bonjour")
    i=i+1
# 1. La boucle While (Tant que)
# La boucle while continue de s'exécuter tant que la condition est vraie (True)

import time

print("--- Exemple 1: Boucle While simple ---")
compteur = 1
while compteur <= 5:
    print(f"Tour de boucle numéro: {compteur}")
    compteur = compteur + 1  # Important: Incrémenter pour changer la condition
print("Fin de la boucle simple.")


# 2. La boucle Infinie
# Une boucle devient infinie si la condition reste toujours vraie.
# ATTENTION : Si vous décommentez les lignes ci-dessous, le programme ne s'arrêtera jamais !
# (Utilisez 'Ctrl+C' dans le terminal pour arrêter une boucle infinie)

print("\n--- Exemple 2: Boucle Infinie (mis en commentaire par sécurité) ---")
# while True:
#     print("Ceci est une boucle infinie !")
#     time.sleep(1) # Ralentit l'affichage pour voir ce qui se passe


# 3. La boucle "Correcte" (Contrôlée)
# Comment écrire une boucle correctement pour éviter qu'elle soit infinie par erreur
# Ou comment utiliser une boucle "infinie" volontaire mais avec une condition d'arrêt (break)

print("\n--- Exemple 3: Boucle Correcte (avec sortie contrôlée) ---")

mot_de_passe = ""
# On demande un mot de passe tant qu'il n'est pas correct
# C'est une utilisation très courante de while
while mot_de_passe != "secret":
    mot_de_passe = input("Entrez le mot de passe (tapez 'secret' pour sortir) : ")
    if mot_de_passe != "secret":
        print("Mot de passe incorrect, réessayez.")

print("Accès autorisé ! Vous avez écrit une boucle correcte.")
