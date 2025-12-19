"""
🟢 1. Einfache Aufgabe / Lösung!
"""
counter = 0

while True:
    try:
        counter += 1
        print(counter)
    except KeyboardInterrupt:
        print("KeyboardInterrupt abgefangen")
        break

