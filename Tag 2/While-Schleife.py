# 🧠 Aufgabe 2: While-Schleife mit break
# Gib Zahlen von 1 bis 10 aus. Stoppe bei 5.

aktuelleZahl = 1

while aktuelleZahl <= 10:               #solange kleiner 10 ist, wird ausgeführt
    print(aktuelleZahl)

    if aktuelleZahl == 9:               # wenn aktuelle zahl den wert 9 entspricht wird abgebrochen,
        break                           # zähler bleibt dann entsprechend stehen
    aktuelleZahl = aktuelleZahl + 1     #aktuelle zahl wird um 1 erhöt
