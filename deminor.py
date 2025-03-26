import random
import sys

tableau2 = []
taille = 0

val = int(input("1 - facile | 2 - moyen | 3 - difficile : "))
if val == 1:
    while taille < 25:
        tableau2.append("V")
        bombe = 5
        taille += 1
if val == 2:
    while taille < 100:
        tableau2.append("V")
        taille += 1
        bombe = 20
if val == 3:
    while taille < 225:
        tableau2.append("V")
        taille += 1
        bombe = 50

def minage(tableau, bombe):
    i = 0
    while i < bombe:
        index = random.randint(0, len(tableau) - 1)
        if tableau[index] == "V":
            tableau[index] = "B"
            i += 1
    for k in range(len(tableau2)):
        if (k + 1) % (5 * val) == 0:
            if tableau2[k] == "B":
                 sys.stdout.write("|X|\n")
            else :
                sys.stdout.write("| |\n")
        else :
            if tableau2[k] == "B":
                 sys.stdout.write("|X|")
            else :
                sys.stdout.write("| |")
    print("------------------------")

loose = False
first = True

def tableau_vide(tableau):
    for i in range(len(tableau)):
        if tableau[i] == "V":
            return 0
        if i == len(tableau):
            return 1

def deminage_simple(tableau, val):
    for i in range(len(tableau)):
        if (i + 1) % (5 * val) == 0:
            if tableau[i] == "D":
                sys.stdout.write("|O|\n")
            else :
                sys.stdout.write("| |\n")
        else :
            if tableau[i] == "D":
                sys.stdout.write("|O|")
            else :
                sys.stdout.write("| |")

while tableau_vide(tableau2) == 0 and loose == False:
    print(tableau2)
    demineur = int(input("Rentré une valeur : "))
    if tableau2[demineur - 1] == "V":
        tableau2[demineur - 1] = "D"
        if first :
            minage(tableau2, bombe)
            first = False
        deminage_simple(tableau2, val)
    elif tableau2[demineur - 1] == "B":
        loose = True
        print("Boom")