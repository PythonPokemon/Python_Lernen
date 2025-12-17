"""
🟢 2. Einfache Aufgabe / Lösung!
"""


try:
    zahlen = [10, 20, 30]
    index = 5             # gültig wären nur: 0, 1, 2

    print(zahlen[index])  # führt zu IndexError

except IndexError:
    print("❌ Fehler: Dieser Listenindex existiert nicht!")
