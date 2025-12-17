"""
🟢 3. Einfache Aufgabe / Lösung!

"""


try:
    text = input("Gib ein Wort ein: ")
    print(text.wert)    # String hat kein Attribut '.wert'

except AttributeError:
    print("❌ Fehler: Dieses Objekt besitzt dieses Attribut nicht!")
