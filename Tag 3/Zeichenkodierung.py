""" 
Zeichenkodierung (ASCII, Unicode, UTF-8)
📌 Was ist das?
Ein Computer speichert Buchstaben als Zahlen.
Jeder Buchstabe hat einen sogenannten Code Point.
"""

print(ord("A"))   # → 65 (ASCII)
print(chr(9786))  # → ☺ (Unicode)

# Escape-Sequenz: z. B. \n (neue Zeile), \t (Tab)
print("Hallo\nWelt!")  # Zeilenumbruch
