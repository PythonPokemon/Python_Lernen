"""
🟢 2. Einfache Aufgabe / Lösung!
"""


try:
    text = "abc"            # teste auch: "25"
    zahl = int(text)        # führt zu ValueError bei "abc"
    print(zahl)

except ValueError:
    print("❌ Fehler: Diese Zeichenkette kann nicht in eine Zahl umgewandelt werden!")
