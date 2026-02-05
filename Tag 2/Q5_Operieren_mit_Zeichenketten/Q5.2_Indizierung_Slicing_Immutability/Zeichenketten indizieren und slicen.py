# 🧠 Aufgabe 11: Index und Bereich eines Textes anzeigen
# Gib den ersten Buchstaben und die ersten 3 Buchstaben aus.

wort = "Python"
print(wort[0])      # Erster Buchstabe
print(wort[0:3])    # Erste drei Buchstaben

# umgekehrt
print(wort[-1])     # Letzter Buchstabe

# -----------------------------------------------------------------

liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(liste[0])     # Erster Wert
print(liste[0:3])   # Erste drei Werte
print(liste[2:11:2])  # Werte von Index 2 bis 10 mit Schrittweite 2

# umgekehrt
print(wort[-1])     # Letzter Buchstabe
print(wort[-3:])    # Letzte drei Buchstaben
print(liste[-1])    # Letzter Wert