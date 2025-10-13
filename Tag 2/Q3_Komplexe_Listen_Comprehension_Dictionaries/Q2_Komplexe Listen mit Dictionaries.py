""" 
🧪 Thema: Komplexe Listen mit Dictionaries
🧠 Ziel: Erstelle eine Liste von Dictionaries, wobei jede Person ein Dictionary ist mit Name, Alter und ob sie volljährig ist.

Ein Dictionary (auf Deutsch: Wörterbuch) ist in Python ein Datentyp, der Werte über sogenannte Schlüssel (Keys) speichert. Du kannst dir ein Dictionary vorstellen wie ein echtes Wörterbuch:

📘 Beispiel aus dem echten Leben:
Im Wörterbuch steht:
"Hund" → "dog"
"Katze" → "cat"

Hier ist:
das deutsche Wort der Schlüssel (key),
und das englische Wort der Wert (value).

✅ Wofür sind Dictionaries gut?
Wenn du Daten mit einem Namen versehen willst.
"""

personen = [
    {"name": "Anna", "alter": 17, "volljährig": False},
    {"name": "Ben", "alter": 21, "volljährig": True},
    {"name": "Clara", "alter": 19, "volljährig": True}
]

# jedes dictionary wird durchlaufen und die Werte werden ausgegeben
for person in personen:
    print("Name:", person["name"])   # referenzvariable 'person' aus der liste mit expliziten attributen ["name"] des dictionaries
    print("Alter:", person["alter"])
    print("Volljährig:", person["volljährig"])
    print("---")
