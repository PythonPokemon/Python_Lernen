"""
🟢 2. Einfache Aufgabe / Lösung!
"""


try:
    a = 7
    b = "Hallo"

    ergebnis = a + b      # teste auch: b * 3 (funktioniert), aber a * b ohne korrekte Reihenfolge erzeugt Fehler
    print(ergebnis)

except TypeError:
    print("❌ Fehler: Falsche Operation zwischen Datentypen!")

