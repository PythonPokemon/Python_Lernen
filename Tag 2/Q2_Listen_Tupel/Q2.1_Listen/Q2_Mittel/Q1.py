"""
🟡 MITTLERE AUFGABE – Listen verändern


🧩 Lernziel:
    - Arbeiten mit Methoden wie append(), remove()
    - Werte durch Index ersetzen

🧠 Merksatz
Methoden, die Objekte verändern:
append()
sort()
reverse()

→ ändern direkt
→ geben meist None zurück
"""

# 🧠 Aufgabe 2: Liste verändern
# Füge neue Elemente hinzu und entferne eines.

tiere = ["Hund", "Katze", "Maus"]

tiere.append("Papagei")    # Neues Element am Ende hinzufügen
# tiere.remove("Maus")       # Element entfernen
# tiere[0] = "Hamster"       # Erstes Element ersetzen

print(tiere)  # ['Hamster', 'Katze', 'Papagei']
