# Modules
# import numpy
import random

# Déclarion matrix
SIZE = 10
a = [[0]*SIZE]*SIZE

# Initialisation matrix
for i in range(SIZE):
    for j in range(SIZE):
        # print(random.randint(0, 1))
        a[i][j] = random.randint(0, 1)
print(a)