"""
🟢 1. Einfache Aufgabe / Lösung!
"""


try:
    ergebnis = 5 + 10  # teste 5 + 10 | gültig, aber 5 + "abc" erzeugt einen Fehler
    print(ergebnis)
except TypeError:
    print("❌ Fehler: Du kannst keine Zahl und einen Text addieren!")
