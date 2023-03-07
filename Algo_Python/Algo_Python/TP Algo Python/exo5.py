mat_2 = int(input("Entrez l'ordre de la matrice carrée: "))
print(mat_2)
if(mat_2<=5):
    mat_2 = int(input("L'ordre de la matrice doit être supérieur à 5. Veuillez entrer un nouvel ordre: "))
else:
    couleur = input("Choisissez une couleur: Bleu ou Rouge: ")
    while (couleur != "Bleu" and couleur != "Rouge"):
        couleur = input("Couleur non valide. Veuillez choisir entre Bleu ou Rouge: ")
    position = input("Choisissez la position de la couleur: Haut ou Bas: ")
    while(position != "Haut" and position != "Bas"):
        position = input("Position non valide. Veuillez choisir entre Haut ou Bas: ")
matrice = [[0 for x in range(mat_2)] for y in range(mat_2)]
for i in range(mat_2):
    for j in range(mat_2):
            if (position == "Haut" and i < j) or (position == "Bas" and i > j):
                matrice[i][j] = couleur
            else:
                matrice[i][j] = "0"
print("La matrice est: ")
for i in range(mat_2):
        print(*matrice[i])  