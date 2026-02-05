#exmeple 4: evaluation de la note d'un etudiant: tres bien / bien / moyen / passable / insuffisant:
note = int(input("enter the note"))

if note >= 18:
    print("tres bien")
elif note >= 14:
    print("bien")
elif note >= 10:
    print("moyen")
elif note >= 6:
    print("passable")
else:
    print("insuffisant")
