"""
🟢 1. Einfache Aufgabe / Lösung!
"""


try:
    text = "Hallo"
    text.append(" Welt")   # String hat kein append-Attribut
except AttributeError:
    print("❌ Fehler: Dieses Objekt besitzt dieses Attribut nicht!")
