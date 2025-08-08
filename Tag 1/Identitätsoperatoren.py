"""
Thema: Identitätsoperatoren (is / is not)
Ziel: Verständnis, wann zwei Variablen auf dasselbe Objekt im Speicher zeigen.
Hinweis: Identität ≠ Gleichheit (is prüft Speicheradresse, == prüft Wert)
-------------------------------------------------------------------------------
💡 Lernfortschritt in der Datei:

Aufgabe 1: Einfachster Fall – zwei Variablen zeigen auf dasselbe Objekt.
Aufgabe 2: Vergleich von is und ==.
Aufgabe 3: Best Practice zur Prüfung auf None.
Aufgabe 4: Tiefergehendes Verständnis von Python-Optimierungen (Caching / Interning).
"""

# --- Aufgabe 1 (Basis) --------------------------------------
# Prüfe, ob zwei Variablen auf dasselbe Objekt zeigen
a = [1, 2, 3]
b = a
print("Aufgabe 1:")
print(a is b)      # True – b ist nur eine andere Referenz auf dasselbe Objekt
print(a is not b)  # False – sie sind identisch
print()

# --- Aufgabe 2 (leicht) -------------------------------------
# Unterschied zwischen is und == prüfen
c = [1, 2, 3]
d = [1, 2, 3]
print("Aufgabe 2:")
print(c == d)      # True – Werte sind gleich
print(c is d)      # False – aber im Speicher zwei verschiedene Objekte
print()

# --- Aufgabe 3 (mittel) -------------------------------------
# Prüfen, ob None korrekt erkannt wird (Best Practice!)
wert = None
print("Aufgabe 3:")
if wert is None:
    print("Wert ist None (empfohlene Prüfung)")
else:
    print("Wert ist nicht None")
print()

# --- Aufgabe 4 (schwer) -------------------------------------
# Unterschied zwischen kleinen Zahlen, Strings und Listen bei Identität
print("Aufgabe 4:")
x = 256
y = 256
print("256 is 256:", x is y)  # True – kleine int-Werte werden intern gecached

x_big = 257
y_big = 257
print("257 is 257:", x_big is y_big)  # Kann True oder False sein, abhängig von der Python-Implementierung

s1 = "Hallo"
s2 = "Hallo"
print('"Hallo" is "Hallo":', s1 is s2)  # Meist True wegen String-Interning

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print("[1, 2, 3] is [1, 2, 3]:", l1 is l2)  # False – Listen werden immer neu erstellt
