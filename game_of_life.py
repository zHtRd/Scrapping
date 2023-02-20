# Modules
import random

# Déclarion variables
HEIGHT = 5
WIDTH = 5
A = []

# Fonction initialisation tableau
def fillTable():
    # Initialisation matrix
    for row in range(HEIGHT):
        ligne = []
        for column in range(WIDTH):
            # Remplissage 0 ou 1
            ligne.append(random.randint(0, 1))
        A.append(ligne)
        print(str(A[row]))

# Fonction vérification voisins
def checkNeighbor(row, column):
    neighbor = 0
    try:
        if row == 0 and column == 0:
            if A[row][column+1] == 1:
                neighbor += 1
            if A[row+1][column] == 1:
                neighbor += 1
            if A[row+1][column+1] == 1:
                neighbor += 1
        elif row == 0 and column == WIDTH-1:
            if A[row][column-1] == 1:
                neighbor += 1
            if A[row-1][column] == 1:
                neighbor += 1
            if A[row-1][column-1] == 1:
                neighbor += 1
        elif row == 0:
            if A[row][column-1] == 1:
                neighbor += 1
            if A[row][column+1] == 1:
                neighbor += 1
            if A[row+1][column-1] == 1:
                neighbor += 1
            if A[row+1][column] == 1:
                neighbor += 1
            if A[row+1][column+1] == 1:
                neighbor += 1
        elif column == 0:
            if A[row+1][column] == 1:
                neighbor += 1
            if A[row-1][column] == 1:
                neighbor += 1
            if A[row+1][column+1] == 1:
                neighbor += 1
            if A[row][column+1] == 1:
                neighbor += 1
            if A[row-1][column+1] == 1:
                neighbor += 1
        elif row == HEIGHT-1 and column == 0:
            if A[row-1][column] == 1:
                neighbor += 1
            if A[row-1][column+1] == 1:
                neighbor += 1
            if A[row][column+1] == 1:
                neighbor += 1
        elif row == HEIGHT-1 and column == WIDTH-1:
            if A[row-1][column] == 1:
                neighbor += 1
            if A[row-1][column-1] == 1:
                neighbor += 1
            if A[row][column-1] == 1:
                neighbor += 1
        elif row == HEIGHT-1:
            if A[row][column-1] == 1:
                neighbor += 1
            if A[row][column+1] == 1:
                neighbor += 1
            if A[row-1][column-1] == 1:
                neighbor += 1
            if A[row-1][column] == 1:
                neighbor += 1
            if A[row-1][column+1] == 1:
                neighbor += 1
        elif column == WIDTH-1:
            if A[row+1][column] == 1:
                neighbor += 1
            if A[row-1][column] == 1:
                neighbor += 1
            if A[row+1][column-1] == 1:
                neighbor += 1
            if A[row][column-1] == 1:
                neighbor += 1
            if A[row-1][column-1] == 1:
                neighbor += 1
    except:
        print("")

    # print("Case:",A[row][column])
    # print(A[row-1][column-1])
    # print("Neighbors:",neighbor)

# Fonction itèration chaque cellule
def updateTable():
    checkNeighbor(0,0)

# Fonction principale
def main():
    fillTable()
    
    checkNeighbor(0,0)

# Lance programme
main()