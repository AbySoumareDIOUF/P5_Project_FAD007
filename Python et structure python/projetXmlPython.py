import csv
import json
import xml.etree.ElementTree as ET
file="/home/bbeihdiouf/Téléchargements/Donnees_Projet_Python_DataC5.csv"
with open(file,'r') as file:
        reader=csv.DictReader(file)
        dictionnaire=list(reader)
def convert_to_json(data):
    with open('data.json', 'w') as f:
        json.dump(data, f)
def convert_to_xml(data):
    root = ET.Element('data')
    for item in data:
        elem = ET.SubElement(root, 'item')
        for key, val in item.items():
            child_elem = ET.SubElement(elem, key)
            child_elem.text = str(val)
    tree = ET.ElementTree(root)
    tree.write('data.xml')
def open_file(filename):
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("Le fichier spécifié n'existe pas.")
while True:
    print("Que voulez-vous faire ?")
    print("1. Convertir en JSON")
    print("2. Convertir en XML")
    print("0. Quitter")

    choice = input("Entrez votre choix : ")

    if choice == '1':
        convert_to_json(dictionnaire)
        print("Le fichier a été converti en JSON avec succès.")
        while True:
            print("Que voulez-vous faire avec le fichier JSON ?")
            print("1. Ouvrir le fichier")
            print("0. Revenir au menu principal")

            subchoice = input("Entrez votre choix : ")

            if subchoice == '1':
                open_file('data.json')
            elif subchoice == '0':
                break
            else:
                print("Choix invalide.")

    elif choice == '2':
        convert_to_xml(dictionnaire)
        print("Le fichier a été converti en XML avec succès.")
        while True:
            print("Que voulez-vous faire avec le fichier XML ?")
            print("1. Ouvrir le fichier")
            print("0. Revenir au menu principal")

            subchoice = input("Entrez votre choix : ")

            if subchoice == '1':
                open_file('data.xml')
            elif subchoice == '0':
                break
            else:
                print("Choix invalide.")

    elif choice == '0':
        break
    else:
        print("Choix invalide.")