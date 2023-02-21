# Modules
import random
import time

# Déclarion variables
HEIGHT = 10
WIDTH = 10

# Fonction initialisation tableau
def fillTable(t):
    # Initialisation matrix
    for row in range(HEIGHT):
        ligne = []
        for column in range(WIDTH):
            # Remplissage 0 ou 1
            ligne.append(random.randint(0, 1))
        t.append(ligne)
        # print(str(A[row]))

# Fonction copie d'un tableau 
def copyTable(t):
    newTable = []
    for row in range(HEIGHT):
        ligne = []
        for column in range(WIDTH):
            ligne.append(t[column])
        newTable.append(ligne)
    return newTable

# Fonction vérification voisins d'une cellule
def checkNeighbor(t, row, column):
    neighbor = 0
    try:
        if row == 0 and column == 0:
            if t[row][column+1] == 1:
                neighbor += 1
            if t[row+1][column] == 1:
                neighbor += 1
            if t[row+1][column+1] == 1:
                neighbor += 1
        elif row == 0 and column == WIDTH-1:
            if t[row][column-1] == 1:
                neighbor += 1
            if t[row+1][column] == 1:
                neighbor += 1
            if t[row+1][column-1] == 1:
                neighbor += 1
        elif row == HEIGHT-1 and column == 0:
            if t[row-1][column] == 1:
                neighbor += 1
            if t[row-1][column+1] == 1:
                neighbor += 1
            if t[row][column+1] == 1:
                neighbor += 1
        elif row == HEIGHT-1 and column == WIDTH-1:
            if t[row-1][column] == 1:
                neighbor += 1
            if t[row-1][column-1] == 1:
                neighbor += 1
            if t[row][column-1] == 1:
                neighbor += 1
        elif row == 0:
            if t[row][column-1] == 1:
                neighbor += 1
            if t[row][column+1] == 1:
                neighbor += 1
            if t[row+1][column-1] == 1:
                neighbor += 1
            if t[row+1][column] == 1:
                neighbor += 1
            if t[row+1][column+1] == 1:
                neighbor += 1
        elif column == 0:
            if t[row+1][column] == 1:
                neighbor += 1
            if t[row-1][column] == 1:
                neighbor += 1
            if t[row+1][column+1] == 1:
                neighbor += 1
            if t[row][column+1] == 1:
                neighbor += 1
            if t[row-1][column+1] == 1:
                neighbor += 1
        elif row == HEIGHT-1:
            if t[row][column-1] == 1:
                neighbor += 1
            if t[row][column+1] == 1:
                neighbor += 1
            if t[row-1][column-1] == 1:
                neighbor += 1
            if t[row-1][column] == 1:
                neighbor += 1
            if t[row-1][column+1] == 1:
                neighbor += 1
        elif column == WIDTH-1:
            if t[row+1][column] == 1:
                neighbor += 1
            if t[row-1][column] == 1:
                neighbor += 1
            if t[row+1][column-1] == 1:
                neighbor += 1
            if t[row][column-1] == 1:
                neighbor += 1
            if t[row-1][column-1] == 1:
                neighbor += 1
        else:
            if t[row][column-1] == 1:
                neighbor += 1
            if t[row-1][column-1] == 1:
                neighbor += 1
            if t[row-1][column] == 1:
                neighbor += 1
            if t[row-1][column+1] == 1:
                neighbor += 1
            if t[row][column+1] == 1:
                neighbor += 1
            if t[row+1][column+1] == 1:
                neighbor += 1
            if t[row+1][column] == 1:
                neighbor += 1
            if t[row+1][column-1] == 1:
                neighbor += 1
    except:
        print("Erreur lors du check de voisins")
    # print(row,column,"-->",neighbor)
    return neighbor

# Fonction itération chaque cellule
def updateTable(t):
    newTable = copyTable(t)
    for row in range(HEIGHT):
        for column in range(WIDTH):
            neighbor = checkNeighbor(t, row,column)
            if 2 <= neighbor <= 3: 
                newTable[row][column] = 1
            else:
                newTable[row][column] = 0   
    return newTable 

# Focntion affichage de tableau
def showTable(t):
    for row in range(HEIGHT):
        print(str(t[row]))
# Fonction bel affichage tableau
def showTablePretty(t):
    print("# - - - - - - - - - - #")
    for row in range(HEIGHT):
        ligne = "| "
        for column in range(WIDTH):
            if t[row][column] == 1:
                ligne += "0 "
            else:
                ligne += "  "
        ligne += "|"
        print(ligne)
    print("# - - - - - - - - - - #")

# Fonction principale
def main():
    table = []
    fillTable(table)
    showTablePretty(table)
    print("")
    time.sleep(0.5)

    while True:
        table = updateTable(table)
        showTablePretty(table)
        print("")
        time.sleep(1)

# Lance programme
main()