def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur : Division par zéro"

def calculatrice():
    while True:
        print("\n--- Menu Calculatrice ---")
        print("1. Addition")
        print("2. Soustraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quitter")
        
        choix = input("Choisissez une opération (1-5) : ")

        if choix == "5":
            print("Au revoir !")
            break

        if choix in ["1", "2", "3", "4"]:
            num1 = float(input("Entrez le premier nombre : "))
            num2 = float(input("Entrez le deuxième nombre : "))

            if choix == "1":
                print(f"Résultat : {addition(num1, num2)}")
            elif choix == "2":
                print(f"Résultat : {soustraction(num1, num2)}")
            elif choix == "3":
                print(f"Résultat : {multiplication(num1, num2)}")
            elif choix == "4":
                print(f"Résultat : {division(num1, num2)}")
        else:
            print("Choix invalide.")

calculatrice()
