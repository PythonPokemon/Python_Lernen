""" 
Falsche Operation zwischen Datentypen
"""


try:
    ergebnis = 5 + "ab"
    print(ergebnis)
except TypeError:
    print("falscher datentyp")