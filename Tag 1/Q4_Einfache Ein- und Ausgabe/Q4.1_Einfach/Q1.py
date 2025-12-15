# Aufgabe 1: Begrüßung
# Frage den Benutzer nach seinem Namen und gib eine personalisierte Begrüßung aus.
# inpu() == default type string

name = input("Wie heißt du? ")
print("Hallo, " + name + "! Willkommen im Python-Kurs.")

print("I\'m R2D2")  # mit dem escabe charakter \ kann man hinterher sonderzeichen als literall einsetzen
print(R"I\'m R2D2") # Raw String | Das R sagt Python: „Nichts escapen, alles roh drucken.“

print("abc", end="")            # 'end' == kein zeilenumbruch
print("defg", "hijk", sep="-")  # 'sep' == zwischen den strings, separate zeichen!