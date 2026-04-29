"""
🟠 Schwere Aufgabe
Zweites Vorkommen eines Zeichens suchen

🧩 Lernziel: Durch Angabe eines Startindex kann man gezielt nach weiteren Vorkommen suchen.
"""

wort = "Regenschauer"
erste_position = wort.index("e")                   # Erstes 'e'
zweite_position = wort.index("e", erste_position + 1)  # Suche ab nächstem Index
print("Erstes e:", erste_position)
print("Zweites e:", zweite_position)


