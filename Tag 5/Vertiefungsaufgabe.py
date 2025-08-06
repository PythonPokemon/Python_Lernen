# Vertiefungsaufgabe: Kombi aller Themen

# Ziel: Liste von Zahlen analysieren
zahlen = [5, 0, 12, -3, 7]

for zahl in zahlen:
    try:
        print(f"Zahl: {zahl}")
        ergebnis = 100 / zahl
        print("100 geteilt durch Zahl:", ergebnis)

        if ergebnis > 20:
            print("Hinweis: Ergebnis ist größer als 20.")
        else:
            print("Ergebnis ist in Ordnung.")

    except ZeroDivisionError:
        print("Fehler: Division durch 0.")
    except Exception as e:
        print("Ein unerwarteter Fehler ist aufgetreten:", e)
