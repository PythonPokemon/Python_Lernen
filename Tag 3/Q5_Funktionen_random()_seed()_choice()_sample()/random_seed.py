"""
Festlegen des Zufalls-Startwertes (Seed)
Funktion: random.seed()
Gleicher Seed => gleiche Zufallszahlenfolge

"""

import random

def zufallszahlen_mit_seed():
    random.seed(42)  # Startzustand des Zufallszahlengenerators.
    print(random.random())  # Erster Wert
    print(random.random())  # Zweiter Wert

# Testaufruf
zufallszahlen_mit_seed()

