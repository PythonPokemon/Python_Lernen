# vergleichsoperatoren_aufgaben.py
"""
Thema: Vergleichsoperatoren
Ziel: Werte und Variablen mit ==, !=, >, <, >=, <= vergleichen lernen.

💡 Aufbau der Aufgaben:

Aufgabe 1: Grundlegende Vergleiche mit Zahlen.
Aufgabe 2: Variablenvergleiche für dynamische Werte.
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

print(alter >= min_alter)  # True, da 18 größer ist als 16
print(alter <= max_alter)  # True, da 18 kleiner ist als 65
print(alter != 21)         # True, da 18 ungleich 21
print()
