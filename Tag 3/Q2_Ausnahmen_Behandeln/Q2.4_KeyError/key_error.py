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
    daten = {"name": "Max", "alter": 25, 1:2, 3.3:4.44444}
    print(daten[2])   # teste: 'name', 'alter', 1, 3.3 | wenn keine fehlerausgabe kommt, ist der schlüssel vorhanden.
except KeyError:
    print("❌ Fehler: Dieser Schlüssel existiert nicht im Dictionary!")