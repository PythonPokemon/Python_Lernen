""" 
1,1
1,2
---------
2,1
2,2
---------
3,1
3,2
3,3

"""
zahlenListe1 = [1, 2, 3]
zahlenListe2 = [1, 2]

for zahl1 in zahlenListe1:
    for zahl2 in zahlenListe2:
        # Schritt 1: Ausgabe der aktuellen Zahlen
        print(f"zahlenListe1: {zahl1}  zahlenListe2: {zahl2}")

        # Schritt 2: Berechnung der Multiplikation
        ergebnis = zahl1 * zahl2

        # Schritt 3: Schritt-für-Schritt-Ausgabe
        print(f"Schritt: {zahl1} x {zahl2} = {ergebnis}")
        
        # Leerzeile für bessere Lesbarkeit
        print()
