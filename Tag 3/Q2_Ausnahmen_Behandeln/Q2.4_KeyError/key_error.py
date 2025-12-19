""" 
KeyError: Zugriff auf einen falschen Schlüssel im Dictionary

erklärung dictionary:
variable: die das dictionary speichert
    |
    |       {}  key:    values innerhalb der geschweiften klammer deklariert unser disctionary. Bsp: {key : value}
    |       |   |       |
    |       |   |       |
daten =     {"name": "Max", "alter": 25}

"""

try:
     daten = {"name": "Max", 1:2}
     print(daten[1])
except KeyError:
     print("fehler abgefangen:-)")
