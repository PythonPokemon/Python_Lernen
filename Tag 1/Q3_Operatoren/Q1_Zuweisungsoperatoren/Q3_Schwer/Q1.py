"""
Thema: Zuweisungsoperatoren (Compound Assignment Operators)
Ziel: Verständnis, wie Werte in Variablen verändert werden können.
Operatoren: +=, -=, *=, /=, //=, %=, **=

💡 Lernlogik in den Aufgaben:

Aufgabe 1: Einfache schrittweise Anwendung.
Aufgabe 2: Alle Operatoren einmal durchspielen.
Aufgabe 3: Mehrere Variablen in Kombination - zeigt, dass Operatoren nicht nur mit Konstanten funktionieren.
Aufgabe 4: Realistische Anwendung - hier merkst du, wie praktisch Zuweisungsoperatoren im Alltag sind.
"""
x = 5
print(x)  # Ausgabe: 5
x += 2    # x = x + 2 → 7
print(x)  # Ausgabe: 7
x -= 1    # x = x - 1 → 6
print(x)  # Ausgabe: 6
x *= 3    # x = x * 3 → 18
print(x)  # Ausgabe: 18
x /= 2    # x = x / 2 → 9.0
print(x)  # Ausgabe: 9.0
x //= 2   # x = x // 2 → 4.0
print(x)  # Ausgabe: 4.0
x %= 3    # x = x % 3 → 1.0
print(x)  # Ausgabe: 1.0
x **= 2   # x = x ** 2 → 1.0
print(x)  # Ausgabe: 1.0
    

# --- Aufgabe 1 (Basis) --------------------------------------
# Schrittweise Veränderung einer Zahl
print("Aufgabe 1:")
x = 5
x += 2    # 7
x -= 1    # 6
x *= 3    # 18
x /= 2    # 9.0
print("Endwert von x:", x)
print()

# --- Aufgabe 2 (leicht) -------------------------------------
# Alle Operatoren einmal ausprobieren
print("Aufgabe 2:")
y = 10
y //= 3   # 3
y %= 2    # 1
y **= 3   # 1
print("Endwert von y:", y)
print()

# --- Aufgabe 3 (mittel) -------------------------------------
# Zuweisungsoperatoren in einer Berechnung mit mehreren Variablen
print("Aufgabe 3:")
a = 4
b = 2
a *= b        # a = 8
b += a        # b = 10
a //= b       # a = 0
print("a:", a, "b:", b)
print()

# --- Aufgabe 4 (schwer) -------------------------------------
# Praxisbeispiel: Kontostand-Berechnung mit Zuweisungsoperatoren
print("Aufgabe 4:")
kontostand = 1000.0

# Einzahlung
kontostand += 250.0  # +250€
# Abhebung
kontostand -= 120.0  # -120€
# Jahreszins 3%
kontostand *= 1.03
# Gebühren pro Quartal (4x 5€)
kontostand -= 4 * 5
# Abrunden auf ganze Euro
kontostand //= 1

print("Kontostand am Jahresende:", kontostand, "Euro")
