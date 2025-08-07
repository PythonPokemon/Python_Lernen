""" 
🧪 Thema: Komplexe Listen mit List Comprehensions erstellen
🧠 Ziel: Erstelle eine Liste mit Zahlenpaaren (Tupeln), 
wobei die erste Zahl zwischen 1 und 3 liegt und die zweite Zahl zwischen 1 und 3, aber ungleich der ersten ist.
"""

paare = []

for i in range(1, 4):        # i = 1, 2, 3
    for j in range(1, 4):    # j = 1, 2, 3
        if i != j:
            paare.append((i, j))

print(paare)
