""" 
Wie schreibt man ein benutzerdefiniertes Modul mit Konstanten?

Konstanten können nachdem initialisieren nicht mehr verändert werden!?

in Python gibt es keine echten Konstanten sondern nur Konventionen.!!!
"""

PI = 3.14159
NAME = "Mathe-Modul"    # konstante wierd in Großbuchstaben geschrieben

print(PI)

PI = 3.11111
print(PI)  # Der Wert von PI wurde verändert, obwohl es eine Konstante sein soll!