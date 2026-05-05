"""
🟢 Einfache Aufgabe
Neue sortierte Zahlenliste erstellen

🧩 Lernziel: .sorted() gibt eine neue Liste zurück, ohne die ursprüngliche zu verändern.
"""

zahlen = [5, 3, 9, 1]
sortierte_zahlen = sorted(zahlen)           # Erstellt eine neue sortierte Liste!
print("Original:", zahlen)                  # Original bleibt unverändert
print("Sortiert:", sortierte_zahlen)        # Ausgabe: 

print(id(zahlen))                           # 2598663272960 Speicheradresse
print(id(sortierte_zahlen))                 # 2397081497536 Speicheradresse == neues Objekt!
print(zahlen == sortierte_zahlen)           # '==' prüft ob werte identisch sind
print(zahlen is sortierte_zahlen)           # 'is' prüft ob referenz zum objekt identisch ist