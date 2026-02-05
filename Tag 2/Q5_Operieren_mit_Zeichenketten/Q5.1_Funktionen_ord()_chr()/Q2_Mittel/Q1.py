"""
Aufgabe:

Was wird hier ausgegeben?
"""

zeichen = "F"
zahl = ord(zeichen)

neu = chr(zahl + 2)

print(zeichen)          # Ausgabe: F
print(zahl)             # Ausgabe: 70
print(neu)              # Ausgabe: H
print(zeichen, zahl, neu)  # Ausgabe: F 70 H