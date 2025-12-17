"""
🟢 3. Einfache Aufgabe / Lösung!

"""


try:
    liste = ["Apfel", "Banane", "Kirsche"]
    index = int(input("Gib einen Index ein: "))

    print(liste[index])

except IndexError:
    print("❌ Fehler: Dieser Listenindex existiert nicht!")
