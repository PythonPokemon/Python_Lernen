"""
🟢 2. Einfache Aufgabe / Lösung!
"""


try:
    personen = {"vorname": "Julia", "stadt": "Berlin"}
    schluessel = "alter"       # gültig wären nur: 'vorname', 'stadt'

    print(personen[schluessel])

except KeyError:
    print("❌ Fehler: Dieser Schlüssel existiert nicht im Dictionary!")
