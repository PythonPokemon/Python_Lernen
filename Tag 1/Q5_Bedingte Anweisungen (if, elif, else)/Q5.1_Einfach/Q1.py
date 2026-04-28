"""
🟢 EINFACHE AUFGABEN (if / else)

(Ziel: Grundverständnis für Bedingungen entwickeln)
"""

# Aufgabe 1: Zahl prüfen (positiv / negativ / null)
zahl = int(input("Gib eine Zahl ein: "))

if zahl > 0:
    print("Die Zahl ist positiv.")  # trifft zu, wenn Zahl größer als 0 ist
elif zahl < 0:
    print("Die Zahl ist negativ.")  # trifft zu, wenn Zahl kleiner als 0 ist, bsp. negiert -1
else:
    print("Die Zahl ist null.")     # trifft zu, wenn Zahl genau 0 ist
