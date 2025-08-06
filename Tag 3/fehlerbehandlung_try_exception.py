""" 
📌 Warum Fehler behandeln?
Damit dein Programm nicht abstürzt, wenn etwas Unerwartetes passiert.
"""
# bsp. 1    ----------------------------------------------------------------
try:
    zahl = int(input("Gib eine Zahl ein: "))
    print("Deine Zahl ist:", zahl)
except ValueError:
    print("Das war keine gültige Zahl!")

# bsp. 2    ----------------------------------------------------------------
""" 
📌 Was ist eine Exception?
Ein Fehler, der beim Ausführen des Programms auftritt.
Alle Fehler erben vom Typ BaseException.
"""
try:
    liste = [1, 2, 3]
    print(liste[5])  # IndexError, weil es keinen index 5 gibt
except IndexError:
    print("Diese Position gibt es nicht!")

# bsp. 3    ----------------------------------------------------------------
""" 
Fehler weitergeben (Exception weiterreichen)
"""

def teile(a, b):
    if b == 0:
        raise ZeroDivisionError("Durch null teilen geht nicht!")
    return a / b

try:
    print(teile(10, 0))
except ZeroDivisionError as fehler:
    print("Fehler:", fehler)
