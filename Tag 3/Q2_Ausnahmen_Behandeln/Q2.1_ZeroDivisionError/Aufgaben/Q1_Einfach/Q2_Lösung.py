try:
    a = int(input("Gib eine Zahl ein: "))
    b = int(input("Gib eine zweite Zahl ein: "))

    ergebnis = a / b
    print("Ergebnis:", ergebnis)

except ZeroDivisionError:
    print("❌ Fehler: Durch Null darf man nicht teilen!")
