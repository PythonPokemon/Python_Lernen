"""
🟢 EINFACHE AUFGABE – Grundverständnis zweidimensionaler Schleifen

🧠 Lernziel:
    - Verständnis für doppelte Indizes ([i][j])
    - Verschachtelte Schleifen über Listen von Listen
"""

# Aufgabe: Gib den Inhalt einer 2D-Liste aus (Matrix 2x2)

# Spalte:    0  1 ..... <-->
zahlen = [
            [1, 2],   # Zeile 0  
            [3, 4]    # Zeile 1      
]                     

for i in range(len(zahlen)):             # Äußere Schleife → Zeilen (Regale)
    for j in range(len(zahlen[i])):      # Innere Schleife → Spalten (Fächer)
        print("Regal", i, "Fach", j, "enthält Zahl:", zahlen[i][j])
