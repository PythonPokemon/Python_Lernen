"""
🟢 3. Einfache Aufgabe / Lösung!

"""


try:
    a = int(input("Gib die erste Zahl ein: "))
    b = int(input("Gib die zweite Zahl ein: "))

    print("Ergebnis:", a + b)

except ValueError:
    print("❌ Fehler: Mindestens eine Eingabe war keine gültige Zahl!")

