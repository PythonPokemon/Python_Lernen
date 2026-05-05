"""
Von oben nach unten: Zeilenindex → äußere Schleife (<i>) → Regale
Von links nach rechts: Spaltenindex → innere Schleife (<j>) → Fächer

|   Zeile <i> (Regal)   |   Spalte <j> | Fach    |   Spalte <j> | Fach     |
|-----------------------|------------------------|-------------------------|
|   [0]       (Zeile)   | Hund [0][0]  | Fach 0  | Katze [0][1] | Fach 1   |
|-----------------------|------------------------|-------------------------|
|   [1]       (Zeile)   | Maus [1][0]  | Fach 1  | Vogel [1][1] | Fach 1   |
|-----------------------|------------------------|-------------------------|
"""

tiere = [
        ["Hund", "Katze"],   
        ["Maus", "Vogel"]
        ]

for i in range(len(tiere)):            # äußere Schleife → Regale/Zeile
    for j in range(len(tiere[i])):     # innere Schleife → Regal/SPalteFächer
        print(f"In der Regal Zeile: {i}, im Fach {j} befindet sich → {tiere[i][j]}")

# bestimmung der ausgabe durch index: ist 'zeile' [0] und 'spalte' [0]
print(tiere[0][0])  # ?
print(tiere[0][1])  # ?
print(tiere[1][0])  # ?
print(tiere[1][1])  # ?