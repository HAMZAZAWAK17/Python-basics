#Affiche "Hello World" dans la console
print("Hello ODC")


#Variables
#For camelCase:
#--> nomEtudiant="Hamza"
#For snake_case:
#--> nom_etudiant="Hamza"
#For kebab-case:
#--> nom-etudiant="Hamza"


#exemple:
prix_casquette = 20
print("Le prix de casquette est:", prix_casquette,"DH")

#La saisie des données:
nom=input("Entrez votre nom: ")
age=input("Entrez votre age: ")
print("Bonjour", nom,"vous avez", age,"ans")


#changer la valeur de A et B:
A = 5
B = 10

print("A =", A, "B =", B)

temp = A
A = B
B = temp

print("A =", A, "B =", B)


#Les operations arithmetiques:
#Addition:
print("Addition:", A + B)
#Soustraction:
print("Soustraction:", A - B)
#Multiplication:
print("Multiplication:", A * B)
#Division:
print("Division:", A / B)
#Modulo:
print("Modulo:", A % B)
#Exponentiation:
print("Exponentiation:", A ** B)
#Division reelle:
print("Division reelle:", A / B)
#Division entiere:
print("Division entiere:", A // B)


#La somme de 2 nombres saisis par l'utilisateur:
nombre1 = int(input("Entrez le premier nombre: "))
nombre2 = int(input("Entrez le deuxieme nombre: "))
print("La somme de", nombre1, "et", nombre2, "est", nombre1 + nombre2)


#La concatenation de 2 chaines de caracteres:
chaine1 = input("Entrez la premiere chaine: ")
chaine2 = input("Entrez la deuxieme chaine: ")
print("La concatenation de", chaine1, "et", chaine2, "est", chaine1 + chaine2)


#La comparaison avec un resultat qui est boolean:
x = 10
y = 20
print("x =", x, "y =", y)

# Egalité (==)
print("Est-ce que x est egal a y ?", x == y)

# Différence (!=)
print("Est-ce que x est different de y ?", x != y)

# Supérieur et Inférieur
print("Est-ce que x est superieur a y ?", x > y)
print("Est-ce que x est inferieur a y ?", x < y)

# Supérieur ou égal / Inférieur ou égal
print("Est-ce que x est superieur ou egal a 10 ?", x >= 10)
print("Est-ce que x est inferieur ou egal a 15 ?", x <= 15)


#and or not:
print("and:", x > y and x < y)
print("or:", x > y or x < y)
print("not:", not (x > y))


