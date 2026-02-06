
# gibt die werte des dictionarys als variablen aus.
# bestimmt mit [0] den value-Index
dct = {}

# Tupel
# Index:    0  1
#           |  |
dct['1'] = (1, 2)   # index [0] = key '1', value = (1, 2)
dct['2'] = (2, 1)   # index [1] = key '2', value = (2, 1)
dct['3'] = (3, 0)   # index [2] = key '3', value = (3, 0)

for x in dct.keys():
    print(dct[x][0], end="")