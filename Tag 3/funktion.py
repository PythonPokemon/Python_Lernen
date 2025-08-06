"""
📌 Was ist eine Funktion?
Eine Funktion ist ein kleines Programm im Programm, das man mehrfach verwenden kann.
"""
# Bsp. 1
# Wir definieren eine Funktion, die "Hallo!" sagt
def sag_hallo():
    print("Hallo!\n")

sag_hallo()  # Aufruf der Funktion

# Bsp. 2
"""💡 Funktion mit Rückgabewert (return)"""
def verdopple(zahl):
    return zahl * 2  # gibt das Ergebnis zurück

ergebnis = verdopple(5)
print(ergebnis)  # 10
