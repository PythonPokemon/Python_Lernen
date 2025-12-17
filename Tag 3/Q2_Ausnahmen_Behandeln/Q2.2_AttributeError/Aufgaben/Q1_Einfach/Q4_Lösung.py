"""
🟢 2. Einfache Aufgabe
Aufgabe (einfach)

Schreibe ein Programm, das zwei Variablen mit Ganzzahlen definiert und anschließend eine Division durchführt.
Falls die zweite Zahl den Wert 0 hat, soll eine freundliche Fehlermeldung erscheinen.

👉 Verwende try / except.
"""


try:
    a = 10
    b = 0

    ergebnis = a / b
    print("Ergebnis:", ergebnis)

except ZeroDivisionError:
    print("❌ Fehler: Durch Null darf man nicht teilen!")
