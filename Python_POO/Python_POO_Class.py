class validation:
    def __init__(self, numero,nom,prenom,classe,note,datenaissance):
        self.numero = numero
        self.nom = nom
        self.prenom =prenom
        self.classe = classe
        self.note = note
        self.datenaissance = datenaissance
    def validation_numero(self):
        if len(self.numero) != 7 or not self.numero.isupper() and self.numero.isalpha() or self.numero.isdecimal():
            return False
        return self.numero
    def validation_nom(self):
            if (len(self.nom)<=2) and not ("A"<=self.nom[0]<="Z"):
                return False
            return self.nom
    def validation_prenom(self):
            if (len(self.prenom)<3) and not ("A"<=self.prenom[0]<="Z"):
                return False
            return self.prenom
    def validation_classe(self):
        if self.classe =='' or (self.classe[-1] not in ['a', 'b','A','B'] and "6" < self.classe[0] < "3"):
            return False
        return self.classe
        
    def validation_note(self):
        dico={}
        self.note = self.note.split(" ")
        for n in range (len(self.note)):
            k = self.note[n].split('[')
            if len(k)==2:
                matiere = k[0]
                dico[matiere] = []
                self.notes = k[1][:-1]
                self.notes = self.notes.replace(',', '.').replace('|', ':').replace("]","").split(':')
                for i in self.notes:
                    if i =="1à":
                        return False
                    if 20 < float(i) < 0:
                        return False
        return self.note
    def validate_date(self):
        self.datenaissance = self.datenaissance.replace(" ", "/")
        self.datenaissance = self.datenaissance.replace(",", "/")
        self.datenaissance = self.datenaissance.replace(":", "/")
        self.datenaissance = self.datenaissance.replace("-", "/")
        self.datenaissance=self.datenaissance.split("/")
        if len(self.datenaissance)==3:
            jour =(self.datenaissance[0])
            mois =( self.datenaissance[1])
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
            annee =self.datenaissance[2]
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
                    if not (1<=jour<=29 and mois==2 or (mois in [1,5,3,7,8,10,12] and 1<=jour<=31) or (mois in [4,6,10,9] and 1<=jour<=30)):
                        return False
                    if not (1<=jour<=28 and mois==2 or (mois in [1,5,3,7,8,10,12] and 1<=jour<=31)or (mois in [4,6,10,9] and 1<=jour<=30)):                        return False
        return self.datenaissance   
    
            