"""
🟢 1. Einfache Aufgabe / Lösung!
"""


try:
    daten = {"name": "Max", "alter": 25}
    print(daten["stadt"])   # teste 'name' oder 'alter' | 'stadt' existiert nicht
except KeyError:
    print("❌ Fehler: Dieser Schlüssel existiert nicht im Dictionary!")
