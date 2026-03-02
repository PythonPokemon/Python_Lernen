"""
🟢 Einfache Aufgabe: Gib die Namen aller Personen in einer Liste aus.

🧩 Lernziel:
    - Den Zugriff auf Werte in Dictionaries üben.
    - Listen von Dictionaries durchlaufen und Daten extrahieren.
"""

personen = [
    {"name": "Anna", "alter": 17, "volljährig": False},
    {"name": "Ben", "alter": 21, "volljährig": True},
    {"name": "Clara", "alter": 19, "volljährig": True}
]

# Lösung
for person in personen:
    print(person["name"], person["alter"], person["volljährig"])
