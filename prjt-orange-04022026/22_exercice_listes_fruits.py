fruits = ["pomme", "banane", "cerise", "orange", "kiwi"]

print(fruits[0])
print(fruits[-1])
print(fruits[2])

fruits[1] = "mangue"
print(fruits)

fruits.append("ananas")
fruits.insert(0, "fraise")
print(fruits)

fruits.remove("kiwi")
fruits.pop()
print(fruits)

print(fruits[:3])
print(fruits[-2:])

print(len(fruits))

if "banane" in fruits:
    print("Banane est là")

if "peche" in fruits:
    print("Pêche est là")
else:
    print("Pêche n'est pas là")

for fruit in fruits:
    print(fruit)
