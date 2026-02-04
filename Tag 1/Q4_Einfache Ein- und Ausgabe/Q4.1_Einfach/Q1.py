# Aufgabe 1: Begrüßung
# Frage den Benutzer nach seinem Namen und gib eine personalisierte Begrüßung aus.
# inpu() == default type string

name = input("Wie heißt du? ")
print("Hallo, " + name + "! Willkommen im Python-Kurs.")

print("I\'m R2D2")  # mit dem escabe charakter \ kann man hinterher sonderzeichen als literal einsetzen
print(R"I\'m R2D2") # Raw String | Das R sagt Python: „Nichts escapen, alles roh drucken.“

print("abc", end="")            # 'end' == kein zeilenumbruch, nachdem print befehl!
print("defg", "hijk", sep="-|-")  # 'sep' == zwischen den strings, separate zeichen!

# f string == formated string
distance = 234
print(f"die strecke ist {distance}km lang.")


Schuessel = 24
Reifendruck = 2.5
Testperson = "Gustave"
AGeb = "23.05.1995"

print("Der Umfang der Schüssel ist", Schuessel,".", sep="")
print("Der Reifendruck soll", Reifendruck,"Bar sein.")
print("Der RName der Tesperson ist", Testperson,".", sep="")
print("Der Geburtstag von Aline ist am ", AGeb,".", sep="")

fahrt_zeit = 45
pause = 5
print(f" du bist insgesamt {fahrt_zeit + pause} gefahren")  # 45 + 5 == 50 min

