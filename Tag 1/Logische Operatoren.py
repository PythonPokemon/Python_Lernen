# logische_operatoren_aufgaben.py
"""
Thema: Logische Operatoren (and, or, not)
Ziel: Verständnis, wie Wahrheitswerte kombiniert und geprüft werden.
Operatoren: and (UND), or (ODER), not (NICHT)

💡 Lernaufbau der Aufgaben:

Aufgabe 1: Direkte logische Ausdrücke verstehen.
Aufgabe 2: Erste Kombination von Vergleichsoperatoren mit logischen Operatoren.
Aufgabe 3: Anwendung in einer if-Struktur mit einfachen Bedingungen.
Aufgabe 4: Realistisches, verschachteltes Szenario, in dem mehrere Bedingungen gemeinsam geprüft werden.
"""

# --- Aufgabe 1 (Basis) --------------------------------------
# Einfache logische Ausdrücke
print("Aufgabe 1:")
print(True and False)   # UND → False
print(True or False)    # ODER → True
print(not True)         # NICHT → False
print()

# --- Aufgabe 2 (leicht) -------------------------------------
# Mehrere Bedingungen kombinieren
print("Aufgabe 2:")
x = 10
y = 5
print(x > 0 and y > 0)   # True AND True → True
print(x > 0 and y < 0)   # True AND False → False
print(x < 0 or y > 0)    # False OR True → True
print(not (x > y))       # NOT True → False
print()

# --- Aufgabe 3 (mittel) -------------------------------------
# Logische Operatoren in einer if-Bedingung
print("Aufgabe 3:")
alter = 20
ticket = True
mitglied = False

# Bedingung: Eintritt nur, wenn über 18 UND Ticket vorhanden
if alter >= 18 and ticket:
    print("Eintritt erlaubt")
else:
    print("Kein Eintritt")

# Bedingung: Rabatt, wenn unter 18 ODER Mitglied
if alter < 18 or mitglied:
    print("Rabatt gewährt")
else:
    print("Kein Rabatt")
print()

# --- Aufgabe 4 (schwer) -------------------------------------
# Praxisbeispiel: Zugangskontrolle mit verschachtelten Bedingungen
print("Aufgabe 4:")
benutzername = "admin"
passwort_ok = True
zweifaktor_ok = False
ausnahme_code = True

# Zugang erlaubt, wenn:
# - Benutzer ist admin UND Passwort + 2FA ok
# - ODER Ausnahme-Code vorhanden
if (benutzername == "admin" and passwort_ok and zweifaktor_ok) or ausnahme_code:
    print("Zugang erlaubt")
else:
    print("Zugang verweigert")
