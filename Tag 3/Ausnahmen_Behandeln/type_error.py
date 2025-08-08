""" 
Falsche Operation zwischen Datentypen
"""


try:
    ergebnis = 5 + "abc"  # teste 5 + 10 | wenn keine fehlerausgabe kommt, ist die Addition zwischen Zahl und Text nicht erfolgt
except TypeError:
    print("❌ Fehler: Du kannst keine Zahl und einen Text addieren!")
