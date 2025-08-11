# Listen – Erstellen, Index, Methoden

# Liste erstellen
# Index     0       1       2      Länge ist aber 3
#           |       |       |   
farben = ["rot", "grün", "blau"]

# Zugriff
print("Farben vor dem bearbeiten!")
print(farben[0])        # rot
print(farben[1])        # grün
print(farben[2])        # blau

print("wieviel Farben im Index gibt es? == " + str(len(farben)))      # gibt die länge des indexes aus == 3

# Bearbeiten
farben.append("gelb\n")   # .append() fügt hinzu
farben.remove("grün")   # .remove() entfernt
farben[1] = "lila"      # ersetzt

# Durchlaufen
for farbe in farben:
    print("Farbe:", farbe)

print("Farben nach dem bearbeiten!")
print(farben[0])        # rot
print(farben[1])        # grün
print(farben[2])        # blau


