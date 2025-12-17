"""
🟢 3. Einfache Aufgabe / Lösung!

"""


try:
    text = input("Gib ein Wort ein: ")
    ergebnis = text + 5     # Text + Zahl ist nicht erlaubt
    print(ergebnis)

except TypeError:
    print("❌ Fehler: Text und Zahl können nicht kombiniert werden!")
