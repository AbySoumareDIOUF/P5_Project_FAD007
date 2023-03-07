
from Projet_Fonction import validation_numero
from Projet_Fonction import validation_nom
from Projet_Fonction import validation_prenom
from Projet_Fonction import validation_classe
from Projet_Fonction import validation_date
from Projet_Fonction import validation_note
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
les_erreurs = {}
valide = []
non_valide = []
for i in dictionnaire:
    Numero = validation_numero(i["Numero"])
    Nom = validation_nom(i["Nom"])
    Prenom = validation_prenom(i["Prénom"])
    Note = validation_note(i["Note"])
    Classe = validation_classe(i["Classe"])
    Date=validation_date(i["Date de naissance"])
    if Numero == False:
        les_erreurs.setdefault("numero",i["Numero"])
        non_valide.append(i)
    elif Nom == False:
        les_erreurs.setdefault("nom",i["Nom"])
        non_valide.append(i)
    elif Classe == False:
        les_erreurs.setdefault("classe",i["Classe"])
        non_valide.append(i)
    elif Prenom == False:
        les_erreurs.setdefault("prenom",i["Prénom"])
        non_valide.append(i)
    elif Date == False:
        les_erreurs.setdefault("date",i["Date de naissance"])
        non_valide.append(i)
    elif Note == False:
            les_erreurs.setdefault("note",i["Note"])
            non_valide.append(i)
    else:
        valide.append(i)
dico_note ={}

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
    note = xnote      
    i["Note"] = xnote
    if "Date de naissance" in i:
        i["Date de naissance"] = i["Date de naissance"].replace(" ", "/")
        i["Date de naissance"] = i["Date de naissance"].replace(",", "/")
        i["Date de naissance"] = i["Date de naissance"].replace(":", "/")
        i["Date de naissance"] = i["Date de naissance"].replace("-", "/")
  #-------------------------------------------------------------------------------------------------------------------------
  #-------------------------------------------------------------------------------------------------------------------------
def modification(chaine):
    for i in chaine:
        numero = validation_numero
        if numero == False:
            numero = input("Entrer un bon numero")
        else :
            print("ce numero est valide")
        nom = validation_nom
        if nom == False:
            nom = input("entrer un bon nom qui respecte toutes les conditions")
        else:
            print("nom valide")
        prenom = validation_prenom
        if prenom == False:
            prenom = input("entrer un bon prenom")
        else:
            print("prenom valide")
        note = validation_note(i["Note"])
        if note == False:
            note = input("entrer une bonne note, les devoirs seront séparés par | et les examens pas :")
        else:
            print("note valide")
        classe = validation_classe(i["Classe"])
        if classe == False:
            classe =("entrer une classe compris entre 3 et 6 et la derniere lettre est soit A ou B")
        else:
            print("classe valide")
        date=validation_date(i["Date de naissance"])
        if date == False:
            date =("entrer une date avec le format jj/mm/aaaa exemple 18/04/2000")
        else:
            print("date valide")
  #-------------------------------------------------------------------------------------------------------------------------
  #-------------------------------------------------------------------------------------------------------------------------
  
      
def menu():
    try:
        print("MENU".center(180, '*'))
        print("""
                    ...........................................................
                    |    1. Afficher les lignes valides                        |
                    |    2. Afficher Une information par rapport a son numéro  |
                    |    3. Afficher les 5 premiers                            |
                    |    4. Ajouter de nouvelles informations                  |
                    |    5. Modifier une ligne invalides                       |
                    |    6. Revenir au menu principal                          |
                    |    7. Quitter                                            |
                    |..........................................................|
        """)
        try:
            choix = int(input("Faites votre choix: "))
        except Exception as e:
            menu()

        if choix == 1:
            print("""
                ==> a.  Les lignes valides
                
                ==> b.  Les ligne Invalides
                
                ==> c.  Menu principal  
                
                ==> d.  Quiter        
                """)
            choix=input("Que voulez vous afficher?? : ")
            if choix == "a" :
                print("******************************************Les lignes valides***************************************************")
                print(valide)
                menu()
            if choix == "b" :
                print("******************************************Les lignes invalides***************************************************")
                print(non_valide)
                menu()
            if choix =="c" :
                menu()
            if choix == "d" :
                exit()
        elif choix == 2:
            print("Vous desirez afficher les informations de quel étudiant")
            num =input("Saisir un numero d'etudiant : ")
            for i in non_valide:
                if num == i["Numero"]:
                    print(i)
                    menu()
            for i in valide:
                if num == i["Numero"]:
                    print(i)
                    menu()
        elif choix == 3: 
            print(" Voici les cinq premier de la classe : ")
            dictio=dict()
            comparaison = []
            p = 12
            for i in valide:
                comparaison.append(i)
            comparaison.sort(key= lambda x:x["moyenne_general"],reverse=True)
            comparaison = comparaison[:5]
            print(comparaison)
            menu()
        elif choix == 4:
            print("Affichage des cinq premiers".center(140, '-'))
            menu()
        elif choix == 5:
            print("Modification des elements invalides".center(140, '-'))
        elif choix == 6:
            menu()
        elif choix == 7:
            menu()
        else:
            print("Merci de votre visite".center(178, '*'))
            exit()
    except KeyboardInterrupt:
        print()
        print("Merci de votre visite".center(178, '*'))
        print()
        exit()
     
print("""            
      
      
                     __________________________________________________________________
                    |   1.  Afficher toutes les ligne                                  |
                    |        a.  les lignes valides                                    |
                    |       b.  les ligne Invalides                                    |
                    |   2.  Afficher Une information par rapport a son numéro          |
                    |   3.  Afficher les 5 premiers                                    |
    MENU            |   4.  Ajouter de nouvelles informations                          |
                    |   5.  Modifier une ligne invalides                               |
                    |        a.  les ligne Invalides                                   |
                    |       b.  Choisir une ligne Invalide à modifier                  |
                    |   6.  Revenir au menu principal                                  |
                    |   7.  Pour sortir                                                |
                    |__________________________________________________________________|   
                    
                        
    """)
choix=input("Faites votre choix : ")
if choix == "1" : 
    print("""
        ==> a.  Les lignes valides
           
        ==> b.  Les ligne Invalides
         
        ==> c.  Menu principal  
        
        ==> d.  Quiter        
          """)
    choix=input("Que voulez vous afficher?? : ")
    if choix == "a" :
        print("******************************************Les lignes valides***************************************************")
        print(valide)
        menu()
    if choix == "b" :
        print("******************************************Les lignes invalides***************************************************")
        print(non_valide)
        menu()
    if choix =="c" :
        menu()
    if choix == "d" :
        exit()
if choix == "2":
    print("Vous desirez afficher les informations de quel étudiant")
    num =input("Saisir un numero d'etudiant : ")
    for i in non_valide:
        if num == i["Numero"]:
            print(i)
            menu()
    for i in valide:
        if num == i["Numero"]:
            print(i)
            menu()
if choix == "3":
    print(" Voici les cinq premier de la classe : ")
    dictio=dict()
    comparaison = []
    p = 12
    for i in valide:
        comparaison.append(i)
    comparaison.sort(key= lambda x:x["moyenne_general"],reverse=True)
    comparaison = comparaison[:5]
    print(comparaison)
if choix =='4':
    print("Que voulez vous modifier")
    print("""
        ==> a.  Le numero
           
        ==> b.  Le nom
         
        ==> c.  Le prenom  
        
        ==> d.  La classe
        
        ==> e.  La note
        
        ==> f.  La date de naissance        
          """)
    choix=input("Que voulez vous afficher?? : ")
    if choix=="a":
        numero = input("entrer le numero : ")
        for i in non_valide:
            if numero == i["Numero"]:
                numero = input("Entrer un bon numero : ")
            print("ce numero est valide")
        
            
     


    
    

            