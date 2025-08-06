"""
🧠 Warum ist das so wichtig (besonders für Anfänger)?
📦 Du sammelst alle Objekt-Daten an einem Ort (im Konstruktor)
🔍 Du siehst sofort, welche Werte das Objekt bei der Erstellung benötigt
✅ Du vermeidest Fehler, weil du nie mit „nicht existierenden“ Attributen arbeitest
🧱 Es ist die Basis für sauberen OOP-Code (Objektorientierte Programmierung)

🧭 Fazit für Anfänger
✅ Immer alle Attribute mit self im Konstruktor setzen, wenn du möchtest, dass dein Objekt damit dauerhaft arbeiten kann.
-------------------------------------------------------------------------------------------------------------------------
🔁 Warum?
self bedeutet: „Ich meine dieses konkrete Objekt.“
Ohne self arbeitest du nur mit lokalen (temporären) Variablen, die nach der Methode wieder verschwinden.
"""


# ✅ Best Practice: alles im Konstruktor definieren
class Hund:
    def __init__(self, name, rasse, alter):
        self.name = name
        self.rasse = rasse
        self.alter = alter

    def bellen(self):
        print(f"{self.name} bellt!")

    def info(self):
        print(f"Name: {self.name}, Rasse: {self.rasse}, Alter: {self.alter}")

# aufrufen der Klasse
hund1 = Hund("Rex", "Labrador", 5)
hund1.bellen()       # Rex bellt!
hund1.info()         # Name: Rex, Rasse: Labrador, Alter: 5

