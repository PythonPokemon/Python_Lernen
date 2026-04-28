

i = 6

j = 5
 
log1 = i and j  # bedeutte alles über 0 ist true, also wird das letztere ausgegeben
print(log1)

"""
fiktives bsp. da variablen freie werte zugewiesen wurden
                2er potenz
                8 4 2 1
Binär i ==6:    0 | | 0
Binär j ==5:    0 | 0 |
-----------------------
Ergebnis:       0 | 0 0     # für & and als zeichen: also: 0 + 4 + 0 + 0 == 4
Ergebnis:       0 | | |     # für | or, da auch 1 und 1 richtig ist, also: 0 + 4 + 2 + 1 == 7
"""
log2 = i & j    # binär operation

print(log2)
 
log2 = i | j 
print(log2)