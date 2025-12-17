"""
🟢 1. Einfache Aufgabe / Lösung!
"""


try:
    zahl = int(input("Gib eine Zahl ein: "))    # teste: 5, 10, "abc"
    print("Deine Zahl ist:", zahl)
except ValueError:
    print("❌ Fehler: Das war keine gültige Zahl, sondern ein Buchstabe oder ein anderes Zeichen.")
