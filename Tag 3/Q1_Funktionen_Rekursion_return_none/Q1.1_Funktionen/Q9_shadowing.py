"""
Shadowing / Überschattung von Variablen

Wenn eine lokale Variable oder ein Funktionsparameter denselben Namen
wie eine globale Variable hat, wird die globale Variable innerhalb
des lokalen Gültigkeitsbereichs überschattet.

Die lokale Variable ist eigenständig. Änderungen an ihr verändern
die globale Variable nicht.
"""


param1 = 123456789  # globale Variable

def message(param1):
    param1 = 111     # lokale Variable wird neu zugewiesen
    print(param1)

message(1)           # Ausgabe: 111
print(param1)        # Ausgabe: 123456789