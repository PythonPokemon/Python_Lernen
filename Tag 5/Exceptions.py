# ⚠️ 4. Exceptions – Fehler erkennen & behandeln

try:
    zahl = int(input("Gib eine Zahl ein: "))
    print("100 geteilt durch", zahl, "=", 100 / zahl)
    
except ValueError:
    print("Fehler: Bitte gib eine gültige Zahl ein. und keinen buchstaben")
except ZeroDivisionError:
    print("Fehler: Division durch 0 ist nicht erlaubt.")
finally:
    print("Programm beendet.")
