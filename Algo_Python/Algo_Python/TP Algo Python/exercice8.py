nom=str(input("saisir un nom""\n"))
prenom=str(input("saisir un prenom""\n"))
classe=(input("saisir la classe""\n"))
note_dev=float(input("saisir une note de devoir""\n"))
note_projet=float(input("saisir une note de projet""\n"))
note_exam=float(input("saisir une note d'examen""\n"))
tel=int(input("saisir un numero de telephone""\n"))
while len(tel) != 9 and tel[0:2] not in ["77", "78", "76"]:
    print("numero de téléphone incorrect")
    tel=int(input("saisir un bon numero de telephone""\n"))
while  20<=float(note_dev)<= 0:
    note_dev=float(input("saisir une note de devoir compris entre 0 et 20""\n"))
while  20<=float(note_dev) <= 0:
    note_exam=float(input("saisir une note d'examen compris entre 0 et 20""\n"))
while  20<=float(note_dev) <= 0:
    note_projet=float(input("saisir une note de projet compris entre 0 et 20""\n"))
etudiants=[]
la_moyenne = (float(note_dev) + float(note_exam) + float(note_exam)) / 3
etudiant = {
        "tel": tel,
        "nom": nom,
        "prenom": prenom,
        "classe": classe,
        "note de devoir": float(note_dev),
        "note de projet": float(note_projet),
        "note d'examen": float(note_exam),
        "Moyenne": la_moyenne
    }
etudiants.append(etudiant)
for etudiant in etudiants:
        if etudiant["tel"] == tel:
            print("Numéro de téléphone déjà utilisé")

