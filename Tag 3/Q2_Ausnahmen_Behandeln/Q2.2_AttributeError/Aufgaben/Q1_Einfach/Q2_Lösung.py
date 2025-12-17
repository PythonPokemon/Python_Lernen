"""
🟢 1. Einfache Aufgabe / Lösung!
"""


try:
    text = "Hallo"
    print(text.append())   # String hat kein append-Attribut
except AttributeError:
    print("❌ Fehler: Dieses Objekt besitzt dieses Attribut nicht!")
