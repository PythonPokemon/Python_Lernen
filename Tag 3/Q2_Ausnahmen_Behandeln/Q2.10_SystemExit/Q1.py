"""
Was macht SystemExit genau?

SystemExit beendet das Python-Programm.
Es ist keine normale Fehlermeldung, sondern ein kontrollierter Programmabbruch.
--------------------------------------------------------------------------------------
raise SystemExit löst bewusst die Exception SystemExit aus.
SystemExit ist eine spezielle Exception, die direkt von BaseException erbt
und vom Python-Interpreter als Anweisung zum Beenden des Programms interpretiert wird.
"""

# varinate 1 | auskommentieren zum testen
# import sys

counter = 0

while True:
    counter += 1
    print(counter)
    # sys.exit()


# variante 2

# counter = 0

# while True:
#     counter += 1
#     print(counter)
#     raise SystemExit    # raise löst die exception aus
