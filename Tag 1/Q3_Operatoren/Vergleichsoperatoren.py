# vergleichsoperatoren_aufgaben.py
"""
Thema: Vergleichsoperatoren
Ziel: Werte und Variablen mit ==, !=, >, <, >=, <= vergleichen lernen.

💡 Aufbau der Aufgaben:

Aufgabe 1: Grundlegende Vergleiche mit Zahlen.
Aufgabe 2: Variablenvergleiche für dynamische Werte.
Aufgabe 3: Anwendung in einer if-Struktur mit mehreren Zweigen.
Aufgabe 4: Realistisches Beispiel mit String-Vergleich und Zahlenprüfung.
"""

# --- Aufgabe 1 (Basis) --------------------------------------
# Einfache direkte Vergleiche
print("Aufgabe 1:")
print(5 == 5)   # Gleich → True
print(5 != 3)   # Ungleich → True
print(5 > 3)    # Größer → True
print(5 < 3)    # Kleiner → False
print(5 >= 5)   # Größer oder gleich → True
print(3 <= 5)   # Kleiner oder gleich → True
print()

# --- Aufgabe 2 (leicht) -------------------------------------
# Variablen vergleichen
print("Aufgabe 2:")
alter = 18
min_alter = 16
max_alter = 65

print(alter >= min_alter)  # True, da 18 >= 16
print(alter <= max_alter)  # True, da 18 <= 65
print(alter != 21)         # True, da 18 ungleich 21
print()

# --- Aufgabe 3 (mittel) -------------------------------------
# Vergleichsoperatoren in einer if-Bedingung
print("Aufgabe 3:")
temperatur = 22

if temperatur > 25:
    print("Es ist warm.")
elif temperatur >= 15:
    print("Angenehme Temperatur.")
else:
    print("Es ist kühl.")
print()

# --- Aufgabe 4 (schwer) -------------------------------------
# Praxisbeispiel: Login-Prüfung mit Alterskontrolle
print("Aufgabe 4:")
benutzername = "max"
eingabe_name = "Max"
eingabe_alter = 20

# Zugang nur, wenn Name exakt übereinstimmt (Groß-/Kleinschreibung egal) UND Alter >= 18
if benutzername.lower() == eingabe_name.lower() and eingabe_alter >= 18:
    print("Login erfolgreich.")
else:
    print("Login fehlgeschlagen.")
