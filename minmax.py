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
    # lignes
    for ligne in jeu:
        if ligne[0] == ligne[1] == ligne[2] and ligne[0] != " ":
            return 1 if ligne[0] == 'O' else -1

    # colonnes
    for colonne in jeu:
        if jeu[0][colonne] == jeu[1][colonne] == jeu[2][colonne] and jeu[0][colonne] != " ":
            return 1 if jeu[0][colonne] == 'O' else -1

    # diagonales
    if jeu[0][0] == jeu[1][1] == jeu[2][2] and jeu[0][0] != " ":
        return 1 if jeu[0][0] == 'O' else -1
    if jeu[0][2] == jeu[1][1] == jeu[2][0] and jeu[0][2] != " ":
        return 1 if jeu[0][2] == 'O' else -1

    return 0

def minimax(jeu,prof,):
    score_actuel = calcul(jeu)

    if score_actuel == 1 or score_actuel == -1:
        return score_actuel

    if not cases_restante(jeu):
        return 0
    else:
        if

    return 0

n = 10
morpion = [[" " for _ in range(n)] for _ in range(n)]

print("On joue au Morpion !")
print("Tu joues avec 'X' et l'IA joue avec 'O'.")
dessine_morpion(morpion)

