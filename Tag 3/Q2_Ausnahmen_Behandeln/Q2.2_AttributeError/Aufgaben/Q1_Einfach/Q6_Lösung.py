"""
🟢 3. Einfache Aufgabe
Aufgabe (einfach)

Schreibe ein Programm, das den Benutzer nach zwei Zahlen fragt (Benutzereingaben) und anschließend die Division ausführt.
Falls der Benutzer als zweite Zahl 0 eingibt, soll eine freundliche Fehlermeldung erscheinen.

👉 Verwende try / except.
"""


try:
    a = int(input("Gib eine Zahl ein: "))
    b = int(input("Gib eine zweite Zahl ein: "))

    ergebnis = a / b
    print("Ergebnis:", ergebnis)

except ZeroDivisionError:
    print("❌ Fehler: Durch Null darf man nicht teilen!")
