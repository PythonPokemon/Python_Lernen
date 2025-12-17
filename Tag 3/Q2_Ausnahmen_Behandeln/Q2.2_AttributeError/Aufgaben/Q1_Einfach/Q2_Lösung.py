"""
🟢 1. Einfache Aufgabe
Aufgabe (einfach)

Schreibe ein Programm, das eine arithmetische Division direkt in einem print-Befehl ausführt.

Operation: 10 / 0
Da die Division durch 0 nicht erlaubt ist, soll eine freundliche Fehlermeldung ausgegeben werden.

👉 Verwende try / except zum Abfangen des Fehlers.
"""


try:
    print(10/0)
except ZeroDivisionError:
    print("❌ Fehler: Durch Null darf man nicht teilen!")
