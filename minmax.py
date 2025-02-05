import math


# def taille(n):
#     if(n == 3):
#         print("-" * (n*3))
#     if(n == 4):
#         print("-" * (n*3+1))
#     if(n == 5):
#         print("-" * (n*3+2))

def dessine_morpion(jeu):
    for ligne in jeu:
        print(" | ".join(ligne))
        print("-" * (n*3+n-3))
        #taille(len(jeu))

def cases_restante(jeu):
    return any(case == " " for ligne in jeu for case in ligne)

def calcul(jeu):
    n = len(jeu)

    # lignes
    for ligne in range (n):
        if all(case == jeu[ligne][0] and case != " " for case in jeu[ligne]):
            if(jeu[ligne][0] == "O"):
                return 1
            else:
                return -1

        # if ligne[0] == ligne[1] == ligne[2] and ligne[0] != " ":
        #     return 1 if ligne[0] == 'O' else -1

    # colonnes
    for colonne in range(n):
        if all(jeu[ligne][colonne] == jeu[0][colonne] and jeu[ligne][colonne] != " " for ligne in range(n)):
            if(jeu[0][colonne] == "O"):
                return 1
            else:
                return -1
        # if jeu[0][colonne] == jeu[1][colonne] == jeu[2][colonne] and jeu[0][colonne] != " ":
        #     return 1 if jeu[0][colonne] == 'O' else -1

    # diagonales
    if all(jeu[i][i] == jeu[0][0] and jeu[i][i] != " " for i in range(n)):
        if(jeu[0][0] == "O"):
            return 1
        else:
            return -1

    if all(jeu[i][n-1-i] == jeu[0][n-1] and jeu[i][n-1-i] != " " for i in range(n)):
        if (jeu[0][n-1] == "O"):
            return 1
        else:
            return -1

    # if jeu[0][0] == jeu[1][1] == jeu[2][2] and jeu[0][0] != " ":
    #     return 1 if jeu[0][0] == 'O' else -1
    # if jeu[0][2] == jeu[1][1] == jeu[2][0] and jeu[0][2] != " ":
    #     return 1 if jeu[0][2] == 'O' else -1

    return 0

def minimax(jeu,prof,maximize):
    score_actuel = calcul(jeu)

    if score_actuel == 1 or score_actuel == -1:
        return score_actuel

    if not cases_restante(jeu):
        return 0
    
    if maximize:
        best = -math.inf
        for i in range(len(jeu)):
            for j in range(len(jeu)):
                if jeu[i][j] == " ":
                    jeu[i][j] = "O"
                    best = max(best,minimax(jeu,prof+1,False))
                    jeu[i][j] == " "
    else:
        best = math.inf
        for i in range(len(jeu)):
            for j in range(len(jeu)):
                if jeu[i][j] == " ":
                    jeu[i][j] = "X"
                    best = min(best,minimax(jeu,prof+1,False))
                    jeu[i][j] == " "

    return best

def meilleure_position(jeu,joueur):
    best = -math.inf
    m_pos = (-1,-1)

    for i in range(len(jeu)):
        for j in range(len(jeu)):
            if jeu[i][j] == " ":
                jeu[i][j] = joueur
                pos = minimax(jeu,0,joueur == "X")
                jeu[i][j] == " "
                if(pos > m_pos):
                    best = pos
                    m_pos = (i,j)
    return m_pos

n = 10
morpion = [[" " for _ in range(n)] for _ in range(n)]

print("On joue au Morpion !")
print("Tu joues avec 'X' et l'IA joue avec 'O'.")
dessine_morpion(morpion)

while True:
    if cases_restante(jeu) and score_actuel(jeu) == 0:
        print("\nTour du joueur :")
        pos = input().split()


    pass