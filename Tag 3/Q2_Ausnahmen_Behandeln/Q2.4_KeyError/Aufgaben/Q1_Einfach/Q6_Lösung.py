"""
🟢 3. Einfache Aufgabe / Lösung!

"""


try:
    daten = {"tier": "Hund", "farbe": "Braun"}
    schluessel = input("Gib einen Schlüssel ein: ")

    print(daten[schluessel])

except KeyError:
    print("❌ Fehler: Dieser Schlüssel existiert nicht im Dictionary!")
