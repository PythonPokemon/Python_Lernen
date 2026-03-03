"""
🟢 EINFACHE AUFGABE – Zugriff auf Tupel-Elemente

🧩 Lernziel:
    - Verständnis von Indexzugriff in Tupeln
    - Arbeiten mit unveränderlichen Datentypen
"""
# 🧠 Aufgabe 1: Tupel mit Zahlen
# Gib das letzte Element aus dem Tupel aus.

# Index:       0   1   2
zahlenTupel = (10, 20, 30)
zahlenTupel2 = (10, 20, 30)
print(zahlenTupel[2])  # Ausgabe: 

x = zahlenTupel, zahlenTupel2
y = zahlenTupel, zahlenTupel2
print(x)
print( x == y)  # prüft ob werte identisch sind
print( x is y)  # prüft ob referenz zum objekt identisch ist

print(id(x))
print(id(y))