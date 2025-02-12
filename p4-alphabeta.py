import math
import random
import time

def dessine_puissance4(jeu):
    for ligne in jeu:
        print(" | ".join(ligne))
        print("-" * (len(jeu[0]) * 4 - 1))
    print("  ".join(map(str, range(len(jeu[0])))))

def cases_restantes(jeu):
    return any(jeu[0][col] == " " for col in range(len(jeu[0])))

def placer_jeton(jeu,col,jeton):
    for ligne in reversed(jeu):
        if ligne[col] == " ":
            ligne[col] = jeton
            return True
    return False

def retirer_jeton(jeu,col):
    for ligne in jeu:
        if ligne[col] != " ":
            ligne[col] = " "
            break

def calcul(jeu):
    n, m = len(jeu), len(jeu[0])

    # lignes
    for ligne in range(n):
        for col in range(m - 3):
            if jeu[ligne][col] == jeu[ligne][col+1] == jeu[ligne][col+2] == jeu[ligne][col+3] != " ":
                return 1 if jeu[ligne][col] == "O" else -1

    # colonnes
    for col in range(m):
        for ligne in range(n - 3):
            if jeu[ligne][col] == jeu[ligne+1][col] == jeu[ligne+2][col] == jeu[ligne+3][col] != " ":
                return 1 if jeu[ligne][col] == "O" else -1

    # diagonales (haut-gauche à bas-droite)
    for ligne in range(n - 3):
        for col in range(m - 3):
            if jeu[ligne][col] == jeu[ligne+1][col+1] == jeu[ligne+2][col+2] == jeu[ligne+3][col+3] != " ":
                return 1 if jeu[ligne][col] == "O" else -1

    # diagonales (haut-droite à bas-gauche)
    for ligne in range(n - 3):
        for col in range(3, m):
            if jeu[ligne][col] == jeu[ligne+1][col-1] == jeu[ligne+2][col-2] == jeu[ligne+3][col-3] != " ":
                return 1 if jeu[ligne][col] == "O" else -1

    return 0

def alpha_beta(jeu,prof,maximize,alpha,beta,start_time,time_limit=1):
    score_actuel = calcul(jeu)

    if score_actuel == 1 or score_actuel == -1:
        return score_actuel

    if not cases_restantes(jeu):
        return 0

    if time.time() - start_time > time_limit:
        return 0

    if prof > 5:
        return 0

    if maximize:
        best = -math.inf
        for col in range(len(jeu[0])):
            if jeu[0][col] == " ":
                placer_jeton(jeu,col,"O")
                best = max(best,alpha_beta(jeu,prof+1,False,alpha,beta,start_time,time_limit))
                retirer_jeton(jeu,col)
                alpha = max(alpha,best)
                if beta <= alpha:
                    break
        return best
    else:
        best = math.inf
        for col in range(len(jeu[0])):
            if jeu[0][col] == " ":
                placer_jeton(jeu,col,"X")
                best = min(best,alpha_beta(jeu,prof+1,True,alpha,beta,start_time,time_limit))
                retirer_jeton(jeu,col)
                beta = min(beta,best)
                if beta <= alpha:
                    break
        return best

def meilleure_position(jeu):
    best = -math.inf
    m_col = -1

    start_time = time.time()

    for col in range(len(jeu[0])):
        if jeu[0][col] == " ":
            placer_jeton(jeu,col,"O")
            score = alpha_beta(jeu,0,False,-math.inf,math.inf,start_time)
            retirer_jeton(jeu,col)
            if score > best:
                best = score
                m_col = col

            if time.time() - start_time > 1:
                break

    if m_col == -1:
        colonnes_vides = [col for col in range(len(jeu[0])) if jeu[0][col] == " "]
        m_col = random.choice(colonnes_vides)

    return m_col

# --- Main ---
print("\nOn joue au Puissance 4 !")
print("Tu joues avec 'X' et l'IA joue avec 'O'.")

n, m = 6, 7  # Dimensions
puissance4 = [[" " for _ in range(m)] for _ in range(n)]
dessine_puissance4(puissance4)

while True:
    if cases_restantes(puissance4) and calcul(puissance4) == 0:
        print("\nTour du joueur :")
        try:
            col = int(input("Colonne (0-6) : "))
            if 0 <= col < m and puissance4[0][col] == " ":
                placer_jeton(puissance4,col,"X")
                dessine_puissance4(puissance4)
            else:
                print("Colonne invalide ou pleine")
                continue
        except:
            print("Entrée invalide")
            continue

    if calcul(puissance4) == -1:
        print("Joueur a gagné")
        break

    if cases_restantes(puissance4) and calcul(puissance4) == 0:
        print("\nTour de l'IA\n")
        col = meilleure_position(puissance4)
        placer_jeton(puissance4,col,"O")
        dessine_puissance4(puissance4)

    if calcul(puissance4) == 1:
        print("L'IA a gagné")
        break

    if not cases_restantes(puissance4):
        print("Match nul")
        break