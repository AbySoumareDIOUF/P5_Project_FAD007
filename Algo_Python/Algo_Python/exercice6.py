type_couleur = ['rouge', 'vert', 'blanc', 'gris', 'violet', 'bleu']

type_positions = ['ADDP', 'EDDP', 'SDP', 'ADDS', 'EDDS', 'SDS']


position = input("voici les position de couleur : ""\n"
"ADDP, au-dessus de la diagonale principale""\n"
"EDDP, en dessous de la diagonale principale""\n"
"SDP, sur la diagonale principale""\n"
"ADDS, au-dessus de la diagonale secondaire""\n"
"EDDS, en dessous de la diagonale secondaire""\n"
"SDS, sur la diagonale secondaire""\n"
    "choisir une position de couleur : "
)
while (position not in type_positions):
    position = input("position non valide. Veuillez choisir une position parmi la liste ")
couleur = input("voici les couleur : ""\n"
'rouge'"\n"
'vert'"\n"
'blanc'"\n"
'gris'"\n"
'violet'"\n"
'bleu'"\n"
    "choisir une  couleur : "
)
while (couleur not in type_couleur):
        couleur = input("Couleur non valide. Veuillez choisir une couleur parmi la liste ")
mt_2 = int(input("saisir la matrice au carré: "))
while (mt_2 <= 4 ):
        mt_2 = int(input("Donnez un ordre de matrice superieur à 4: "))
matrice = [[0 for x in range(mt_2)] for y in range(mt_2)]
for i in range(mt_2):
        for j in range(mt_2):
            if (position == 'ADDP' and i < j or position == 'EDDP' and i > j or position == 'SDP' and i == j):
                matrice[i][j] = couleur
            elif (position == 'EDDS' and i + j > mt_2 + 1 or position == 'ADDS' and i + j < mt_2 + 1 or position == 'SDS' and i + j == mt_2 + 1):
                matrice[i][j] = couleur
            else:
                matrice[i][j] = "0"
print("La matrice est: ")
for i in range(mt_2):
        print(*matrice[i])  

