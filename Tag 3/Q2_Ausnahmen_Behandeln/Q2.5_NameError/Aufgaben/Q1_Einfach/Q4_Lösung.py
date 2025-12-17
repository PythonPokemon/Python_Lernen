"""
🟢 2. Einfache Aufgabe / Lösung!
"""


try:
    a = 10
    # b = 20    # b ist absichtlich auskommentiert

    print(a)
    print(b)     # führt zu NameError

except NameError:
    print("❌ Fehler: Diese Variable ist nicht definiert!")
