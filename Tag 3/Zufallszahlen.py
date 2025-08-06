import random  # Modul importieren

""" 
Zufallszahlen mit random erzeugen
"""

print(random.random())         # Zufallszahl zwischen 0.0 und 1.0
random.seed(1)                 # Startwert setzen → immer gleiche "Zufallszahl"
print(random.choice([1, 2, 3]))  # Zufälliges Element aus Liste
print(random.sample(range(10), 3))  # 3 zufällige, einzigartige Zahlen aus 0–9
