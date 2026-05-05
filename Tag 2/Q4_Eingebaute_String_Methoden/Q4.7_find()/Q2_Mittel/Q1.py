"""
🟡 Mittlere Aufgabe
Nach einem Teilwort suchen

🧩 Lernziel: .find() funktioniert auch mit Teilstrings und findet deren Startposition im Text.

ps.
zählt auch die leerzeichen mit!
"""

satz = "Ich lerne Python und Python macht Spaß"
position = satz.find("Python")          # Findet das erste 'Python'
print("Position:", position)            # Ausgabe: 10
