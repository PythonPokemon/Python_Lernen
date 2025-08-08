# --- Arithmetische Operatoren ---
print(5 + 3)    # Addition → 8
print(5 - 3)    # Subtraktion → 2
print(5 * 3)    # Multiplikation → 15
print(5 / 2)    # Division (float) → 2.5
print(5 // 2)   # Ganzzahldivision → 2
print(5 % 2)    # Modulo (Rest) → 1
print(2 ** 3)   # Potenzieren → 8

# arithmetik_aufgaben.py

# Aufgabe 1 (Einsteiger):
# Schreibe ein Programm, das zwei Zahlen einliest und dann Addition, Subtraktion, Multiplikation und Division ausgibt.

zahl1 = int(input("Gib die erste Zahl ein: "))
zahl2 = int(input("Gib die zweite Zahl ein: "))

print("Addition:", zahl1 + zahl2)
print("Subtraktion:", zahl1 - zahl2)
print("Multiplikation:", zahl1 * zahl2)
print("Division:", zahl1 / zahl2)  # Achtung: float Division

# Aufgabe 2 (Mittel):
# Erweitere das Programm um Ganzzahldivision (//), Modulo (%) und Potenzieren (**).
# Gib für jede Operation eine Erklärung aus.

print("Ganzzahldivision:", zahl1 // zahl2, "(Ergebnis ohne Nachkommastellen)")
print("Modulo:", zahl1 % zahl2, "(Rest bei der Division)")
print("Potenz:", zahl1 ** zahl2, "(Ergebnis von zahl1 hoch zahl2)")

# Aufgabe 3 (Fortgeschritten):
# Schreibe eine Funktion, die aus zwei Zahlen und einem Operator (+, -, *, /, //, %, **) das Ergebnis berechnet.
# Verwende eine if-elif-else-Struktur.
# Teste die Funktion mit verschiedenen Operatoren.

def berechne(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    elif operator == '//':
        return a // b
    elif operator == '%':
        return a % b
    elif operator == '**':
        return a ** b
    else:
        return "Ungültiger Operator"

print(berechne(5, 3, '+'))
print(berechne(5, 3, '//'))
print(berechne(2, 3, '**'))

# Aufgabe 4 (Experte):
# Erweitere die Funktion so, dass sie Eingabefehler abfängt (z.B. Division durch 0 oder ungültiger Operator).
# Gib passende Fehlermeldungen aus.

def sichere_berechnung(a, b, operator):
    try:
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return a / b
        elif operator == '//':
            return a // b
        elif operator == '%':
            return a % b
        elif operator == '**':
            return a ** b
        else:
            return "Ungültiger Operator"
    except ZeroDivisionError:
        return "Fehler: Division durch 0 ist nicht erlaubt."

print(sichere_berechnung(5, 0, '/'))
print(sichere_berechnung(5, 0, '%'))
print(sichere_berechnung(5, 2, '^'))  # Ungültiger Operator
