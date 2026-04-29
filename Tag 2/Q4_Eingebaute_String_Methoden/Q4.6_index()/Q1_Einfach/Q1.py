"""
🟢 Einfache Aufgabe
Index eines Buchstabens finden

🧩 Lernziel: .index() gibt den Index des ersten Vorkommens eines Zeichens zurück.
Wenn das Zeichen nicht vorhanden ist, entsteht ein ValueError.
"""

wort = "Regenschauer"
position = wort.index("r")        # Findet die Position des ersten 'R'
print("Index von 'R':", position) # Ausgabe: 


# auch mit zahlen möglich
zahlen = [5, 3, 9, 1]
position = zahlen.index(5)
print("index von '5':", position)