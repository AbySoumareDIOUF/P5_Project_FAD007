import re
#validité du numero
def validation_numero(numero):
    if len(numero) != 7 or not numero.isupper():
        return False
    elif numero.isalpha() or numero.isdecimal():
        return False
    return numero
#validation Nom
def validation_nom(nom):
    if (len(nom)<=2):
        return False
    for i in range(1,len(nom)):
        if "A"<=nom[0]<="Z" and "a"<=nom[i]<="z":
            return True
    return nom
#validation prenom
def validation_prenom(prenom):
    if (len(prenom)<3):
        return False
    for i in range(1,len(prenom)):
        if "A"<=prenom[0]<="Z" and "a"<=prenom[i]<="z":
            return True
    return False
#validation classe
def validation_classe(classe):
    if classe =='':
        return False
    if not classe[0].isdigit() or classe[-1].lower() not in ['a', 'b']:
        return False
    if int(classe[0])  > 6 or int(classe[0]) < 3:
        return True
    return classe
#validation Date
def validation_date(date_saisie):
    date_saisie = date_saisie.replace(" ", "/")
    date_saisie = date_saisie.replace(",", "/")
    date_saisie = date_saisie.replace(":", "/")
    date_saisie = date_saisie.replace("-", "/")
    date_saisie=date_saisie.split("/")
    if len(date_saisie)==3:
        jour =(date_saisie[0])
        mois =( date_saisie[1])
        mois_dictionnaire = {
            'janvier': '01',
            'fevrier': '02',
            'fev':'02',
            'mars': '03',
            'avril': '04',
            'mai': '05',
            'juin': '06',
            'juillet': '07',
            'août': '08',
            'aout': '08',
            'septembre': '09',
            'octobre': '10',
            'novembre': '11',
            'décembre': '12',
            'decembre': '12',
            'jan': '01',
            'fev': '02',
            'mar': '03',
            'avr': '04',
            'mai': '05',
            'juin': '06',
            'juil': '07',
            'aou': '08',
            'sep': '09',
            'oct': '10',
            'nov': '11',
            'dec': '12'
        } 
        if mois in mois_dictionnaire:
            mois = int(mois_dictionnaire[mois])
        annee =date_saisie[2]
        an= len(annee)
        for i in annee:
            if i.isalpha():
                return False
        for i in jour:
            if i.isalpha():
                return False
        jour = int(jour)
        if an==4:
          annee = int(annee)
        else:
            if annee >= "23":
                    annee ="19"+annee
            else:
                    annee = "20"+annee
            annee = int (annee)
            if(annee%4==0 and annee%100!=0 or annee%400==0):
                if 1<=jour<=29 and mois==2:
                    return True
                elif mois in [1,5,3,7,8,10,12] and 1<=jour<=31:
                    return True
                elif mois in [4,6,10,9] and 1<=jour<=30:
                    return True
            else:
                if 1<=jour<=28 and mois==2:
                    return True
                elif mois in [1,5,3,7,8,10,12] and 1<=jour<=31:
                    return True
                elif mois in [4,6,10,9] and 1<=jour<=30:
                    return True
    return date_saisie
              
#validation notedef validation_note(note):
def validation_note(note):
    dico={}
    note = note.split(" ")
    for n in range (len(note)):
        k = note[n].split('[')
        if len(k)==2:
            matiere = k[0]
            dico[matiere] = []
            notes = k[1][:-1]
            notes = notes.replace(',', '.').replace('|', '.').split(':')
            for i in notes:
                if "0"<i<"20":
                    return True
                else:
                    return False
    return note
#fonction pour modifier une ligne




