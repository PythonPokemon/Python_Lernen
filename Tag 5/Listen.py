# Listen – Erstellen, Index, Methoden

# Liste erstellen
# Index     0       1       2      Länge ist aber 3
#           |       |       |   
farben = ["rot", "grün", "blau"]

# Zugriff
print(farben[0])        # rot
print(len(farben))      # gibt die länge des indexes aus == 3

# Bearbeiten
farben.append("gelb")   # .append() fügt hinzu
farben.remove("grün")   # .remove() entfernt
farben[1] = "lila"      # ersetzt

# Durchlaufen
for farbe in farben:
    print("Farbe:", farbe)

