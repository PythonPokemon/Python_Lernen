"""
🟢 2. Einfache Aufgabe / Lösung!
"""


try:
    a = 42
    ergebnis = a.upper()    # int hat keine upper()-Methode
    print(ergebnis)

except AttributeError:
    print("❌ Fehler: Dieses Objekt besitzt dieses Attribut nicht!")
