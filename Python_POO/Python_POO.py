from Python_POO_Class import *
import csv
from pprint import pprint
file="/home/bbeihdiouf/Téléchargements/Donnees_Projet_Python_DataC5.csv"
with open(file,'r') as file:
        reader=csv.DictReader(file)
        dictionnaire=list(reader)
        for i in (dictionnaire):
            if "#" not in i["Note"] and i["CODE"]==""or i["Numero"]==""or i["Nom"]==""or i["Prénom"]==""or i["Date de naissance"]==""or i["Classe"]==""or i["Note"]=="":
                continue
            note = i["Note"]
            nouvelle_note=note.replace("#","@")
            i["Note"]=nouvelle_note
            #print(i["CODE"],i["Numero"],i["Nom"],i["Prénom"],i["Date de naissance"],i["Classe"],i["Note"])
valide =[]
non_valide = []
for i in dictionnaire:
    numero =i["Numero"]
    nom = i["Nom"]
    prenom = i["Prénom"]
    classe = i["Classe"]
    note = (i["Note"])
    dateN = (i["Date de naissance"])
    eleve = validation(numero,nom,prenom,classe,note,dateN)
    if eleve.validation_classe() and eleve.validate_date() and eleve.validation_note() and eleve.validation_nom() and eleve.validation_prenom() and eleve.validation_numero():
        valide.append(i)
    else:
        non_valide.append(i)
for i in valide:
    moyenne_generale = 0.0
    if "Note" in i:
        note = i["Note"]
        note = note.split("@")
        num_note = len(note)
        xnote = dict()
    for n in range (len(note)):
            xmatiere = dict()
            k = note[n].split('[')
            if len(k) == 2:
                matiere = k[0]
                notee= k[1][:-1]
                notes=notee.replace(",", ".").split(":")
                devoirs = notes[0].split('|')
            devoir=[float(dev) for dev in devoirs]
            examen = notes[-1].replace("]", "")
            examen = float(examen)
            Moy_Matiere=round((((sum(devoir)/len(devoirs)) + 2*examen)/3),2)
            xmatiere.setdefault('devoirs', devoirs)
            xmatiere.setdefault('examen', examen)
            xmatiere.setdefault('moyenne_matiere', Moy_Matiere)
            moyenne_generale += Moy_Matiere
            xnote.setdefault(matiere, xmatiere)
            moyG =round((moyenne_generale/len(xnote.keys())),2)
            i.setdefault("moyenne_general", moyG)
    print(xnote)
