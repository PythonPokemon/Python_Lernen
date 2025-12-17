"""
🟢 1. Einfache Aufgabe / Lösung!
"""


try:
    liste = [1, 2, 3]
    print(liste[3])     # teste 0, 1, 2 | Index 3 existiert nicht
except IndexError:
    print("❌ Fehler: Dieser Listenindex existiert nicht!")
