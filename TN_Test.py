# Liste und Suchwert festlegen
liste = [5, 12, 7, 3, 9, 3]
gesucht = 3
gefunden = False

# Durch die Liste gehen
for zahl in liste:
    if zahl == gesucht:
        gefunden = True
        

# Ergebnis ausgeben
if gefunden == True:
    print("Gefunden")
else:
    print("Nicht gefunden")