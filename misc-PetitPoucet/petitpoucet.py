#!/usr/local/bin/python3 -u
# -*- coding: utf-8 -*-

import sys
import uuid
import signal
from flag import flag

## Time allowed to complete the challenge (seconds)
DELAY = 90

## Id of current user
curr_id = ""

##
##
##
def p(s, prefix = ""):
        sys.stdout.write(prefix+s)
        sys.stdout.flush()
##
##
##
def err(s, prefix = ""):
        sys.stderr.write(prefix+s)
        sys.stderr.flush()

##
## Handler for the timeout
##
def handler(signum, frame):
    p("Le temps est écoulé!\n")
    err("[!] Le temps est écoulé!\n", "({})  ".format(curr_id))
    sys.exit(0)

##
## Check that a path is valid for the given board
##
def check(board, path):
    DIR_LEFT = "LEFT"
    DIR_RIGHT = "RIGHT"
    DIR_UP = "UP"
    DIR_DOWN = "DOWN"

    b = []
    for row in board:
        b += [ row.split(" ")]

    if len(path) == 0: return False

    curr, path = path[0], path[1:]
    currDir = ""

    ## Then, check that the path is valid
    while len(path):

        ## First check: the first cell must contain "X"
        # if b[curr[0]][curr[1]] != "X":
        #     return False

        next, path = path[0], path[1:]
        if curr == next: return False
        
        # print(" ")
        # for row in b: print(" ".join(row))
        # print(currDir)
        # print(" ")

        if curr[0] == next[0]: ## same row
            mi = min(curr[1], next[1])
            ma = max(curr[1], next[1])
            for c in range(mi+1, ma):
                if b[curr[0]][c] != "-":
                    print("Error: Cell {} not empty.".format((curr[0], c)))
                    return False

            # move is valid
            if curr[1] < next[1]:
                nextDir = DIR_RIGHT
            else:
                nextDir = DIR_LEFT

        elif curr[1] == next[1]: ## same column
            mi = min(curr[0], next[0])
            ma = max(curr[0], next[0])
            for r in range(mi+1, ma):
                if b[r][curr[1]] != "-":
                    print("Error: Cell {} not empty.".format((r, curr[1])))
                    return False

            # move is valid
            if curr[0] < next[0]:
                nextDir = DIR_DOWN
            else:
                nextDir = DIR_UP

        ## cells not sharing any coordinates -> wrong move
        else:
            return False

        ## Check that the direction is not forbidden
        if  currDir == DIR_UP     and nextDir == DIR_DOWN:   return False
        elif currDir == DIR_DOWN  and nextDir == DIR_UP:     return False
        elif currDir == DIR_LEFT  and nextDir == DIR_RIGHT:  return False
        elif currDir == DIR_RIGHT and nextDir == DIR_LEFT:   return False

        ## The move is correct: 1) remove the stone, 2) go on with the next move
        b[curr[0]][curr[1]] = "-"
        curr = next
        currDir = nextDir
        b[curr[0]][curr[1]] = "X"

    # print("=="*8)
    # for row in b: print(" ".join(row))
    # print(" ")

    ## If passed all checks, then the path is valid iif the only stone left on the board is at curr
    for r in range(len(b)):
        for c in range(len(b[0])):
            if r == curr[0] and c == curr[1]: continue
            if b[r][c] != "-":
                return False

    return True

if __name__== "__main__":

    ## Load data
    with open("puzzles.txt") as fp:
        boards = fp.read().split("\n\n")

    boards = [ board.split("\n") for board in boards ]
    boards = boards[:-1]

    curr_id = uuid.uuid4().hex[:8]
    err("[+] New connexion! Number of loaded puzzles: {}\n".format(len(boards)), "({})  ".format(curr_id))

    p("Challenge de programmation!\n")
    p("---------------------------\n")
    p("\n")
    p("Dans ce challenge, tu es sur les traces du Petit Poucet.\n")
    p("Le but est de récupérer tous les cailloux qu'il a semé dans la forêt.\n")
    p("Le premier caillou que tu trouves est représenté par 'X'.\n")
    p("Tous les autres cailloux sont initialement représentés par 'O'.\n")
    p("Par exemple :\n")
    p("    - - -\n")
    p("    O X O\n")
    p("    O - O\n")
    p("\n")
    p("Pour récupérer un caillou, il suffit de se déplacer sur une case marquée\n")
    p("par 'O' pour ramasser automatiquement le caillou : ta nouvelle\n")
    p("position 'X' est alors changée pour cette case.\n")
    p("Si la première position 'X' n'est pas mentionnée, tu peux la choisir.\n")
    p("\n")
    p("Les déplacements se font uniquement sur des lignes et sur des colonnes.\n")
    p("Si tu croises un caillou, tu es obligé de t'arrêter (impossible de \"sauter\"\n")
    p("par dessus un caillou). En arrivant sur une nouvelle case, les règles\n")
    p("de déplacement sont les suivantes :\n")
    p("  - tu peux décider de tourner à gauche ou à droite,\n")
    p("  - tu peux aussi décider de continuer tout droit,\n")
    p("  - en revanche, tu ne peux pas revenir faire marche arrière.\n")
    p("\n")
    p("En nommant les cailloux de l'exemple précédent,\n")
    p("    - - -\n")
    p("    a X d\n")
    p("    b - c\n")
    p("tu peux ramasser les cailloux dans l'ordre X, a, b, c, d.\n")
    p("Il n'est pas possible de ramasser dans l'ordre X, d, c, b (car marche arrière).\n")
    p("\n")
    p("On utilisera des coordonnées pour nommer les cailloux :\n")
    p("   a: (1,0)  ")
    p("   X: (1,1)  ")
    p("   d: (1,2)  ")
    p("   b: (2,0)  ")
    p("   c: (2,2)  ")
    p("\n")
    p("Le chemin qui passe par tous les cailloux est à donner avec une coordonnées par\n")
    p("ligne, et avec une ligne vide pour représenter la fin du chemin. Exemple :\n")
    p("1,1\n")
    p("1,0\n")
    p("2,0\n")
    p("2,2\n")
    p("1,2\n")
    p("\n")
    p("Le Petit Poucet étant taquin, il a semé des cailloux dans plusieurs forêts\n")
    p("de différentes tailles :-)\n")
    p("\n")
    p("Tu as {} secondes pour récupérer les cailloux de toutes les forêts.\n".format(DELAY))
    p("Prêt ? [O/n]\n")
    p(">> ")
    res = sys.stdin.readline().strip()
    if res == "n": sys.exit(0)

    signal.alarm(DELAY)
    signal.signal(signal.SIGALRM, handler)
    try:
        cnt = 0
        for board in boards:
            cnt += 1
            ## Print game
            p("Forêt #{}:\n".format(cnt))
            for row in board: p(row+"\n", " "*4)
            p("\n")

            err("[+] Sending puzzle:\n", "({})  ".format(curr_id))
            for row in board: err(row+"\n", "({})      ".format(curr_id))
            err("\n", "({})  ".format(curr_id))

            ## Read solution
            p("Quel chemin suivre (suite de coordonnées) ?\n")
            path = []
            while True:
                p(">> ")
                res = sys.stdin.readline().strip()
                if res == "": break
                res = res.split(",")
                x, y = int(res[0]), int(res[1])
                path += [(x,y)]

            err("[+] Received path for #{}: {}\n".format(cnt, path), "({})  ".format(curr_id))

            if not check(board, path):
                p("Ce chemin est incorrect.\n")
                p("Bye bye.\n")
                sys.exit(0)
            else:
                err("[+] Solved puzzle #{}\n".format(cnt), "({})  ".format(curr_id))
                p("Tu as récupéré tous les cailloux de cette forêt, bien joué !\n")

        err("[+] Sending the flag.\n", "({})  ".format(curr_id))
        p("Congrats!! Voici le flag :\n{}\n".format(flag))
        sys.exit(0)

    except ValueError: 
        p("Erreur : mauvaise coordonnée.\n")
    else:
        sys.exit(0)
