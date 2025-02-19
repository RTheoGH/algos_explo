import math
import random
import time

def dessine_morpion(jeu):
    n = len(jeu)

    for ligne in jeu:
        print(" | ".join(ligne))
        print("-" * (n * 3 + n - 3))

def cases_restante(jeu):
    return any(case == " " for ligne in jeu for case in ligne)

def calcul(jeu):
    n = len(jeu)

    # lignes
    for ligne in range(n):
        if all(case == jeu[ligne][0] and case != " " for case in jeu[ligne]):
            if jeu[ligne][0] == "O":
                return 1
            else:
                return -1

    # colonnes
    for colonne in range(n):
        if all(jeu[ligne][colonne] == jeu[0][colonne] and jeu[ligne][colonne] != " " for ligne in range(n)):
            if jeu[0][colonne] == "O":
                return 1
            else:
                return -1

    # diagonales
    if all(jeu[i][i] == jeu[0][0] and jeu[i][i] != " " for i in range(n)):
        if jeu[0][0] == "O":
            return 1
        else:
            return -1

    if all(jeu[i][n-1-i] == jeu[0][n-1] and jeu[i][n-1-i] != " " for i in range(n)):
        if jeu[0][n-1] == "O":
            return 1
        else:
            return -1

    return 0

def minimax(jeu,prof,maximize,start_time,time_limit=1):
    n = len(jeu)
    score_actuel = calcul(jeu)

    if score_actuel == 1 or score_actuel == -1:
        return score_actuel

    if not cases_restante(jeu):
        return 0

    if time.time() - start_time > time_limit:
        return 0

    if prof > 5:
        return 0

    if maximize:
        best = -math.inf
        for i in range(n):
            for j in range(n):
                if jeu[i][j] == " ":
                    jeu[i][j] = "O"
                    best = max(best,minimax(jeu,prof+1,False,start_time,time_limit))
                    jeu[i][j] = " "
        return best
    else:
        best = math.inf
        for i in range(n):
            for j in range(n):
                if jeu[i][j] == " ":
                    jeu[i][j] = "X"
                    best = min(best,minimax(jeu,prof+1,True,start_time,time_limit))
                    jeu[i][j] = " "
        return best

def meilleure_position(jeu):
    n = len(jeu)
    best = -math.inf
    m_pos = (-1,-1)

    start_time = time.time()

    for i in range(n):
        for j in range(n):
            if jeu[i][j] == " ":
                jeu[i][j] = "O"
                score = minimax(jeu,0,False,start_time)
                jeu[i][j] = " "
                if score > best:
                    best = score
                    m_pos = (i,j)

            if time.time() - start_time > 1:
                break

    # sécurité récursion infini x)
    if m_pos == (-1,-1):
        cases_vides = [(i,j) for i in range(n) for j in range(n) if jeu[i][j] == " "]
        m_pos = random.choice(cases_vides)

    return m_pos


# --- Main ---
print("\nOn joue au Morpion !")
print("Tu joues avec 'X' et l'IA joue avec 'O'.")

n = int(input("\nTaille du morpion : "))
print("\n")
morpion = [[" " for _ in range(n)] for _ in range(n)]
dessine_morpion(morpion)

while True:
    if cases_restante(morpion) and calcul(morpion) == 0:
        print("\nTour du joueur :")
        pos = input("Position i j : ").split()
        print("\n")
        try:
            i, j = int(pos[0]),int(pos[1])
            if morpion[i][j] == " ":
                morpion[i][j] = "X"
                dessine_morpion(morpion)
            else:
                print("Case occupée")
                continue
        except:
            print("Position invalide")
            continue

    if calcul(morpion) == -1:
        print("Joueur a gagné")
        break

    if cases_restante(morpion) and calcul(morpion) == 0:
        print("\nTour de l'IA\n")
        start_temps_ia = time.time()
        i,j = meilleure_position(morpion)
        print("Temps pris avec minmax : ", time.time()-start_temps_ia, " secondes\n")
        morpion[i][j] = "O"
        dessine_morpion(morpion)

    if calcul(morpion) == 1:
        print("L'IA a gagné")
        break

    if not cases_restante(morpion):
        print("Match nul")
        break