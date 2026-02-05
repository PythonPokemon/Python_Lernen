""" 
📌 Was ist Rekursion?
Eine Funktion, die sich selbst aufruft. Wird oft in Mathe benutzt.

bspl.
fakultaet(4)
= 4 * fakultaet(3)
= 4 * 3 * fakultaet(2)
= 4 * 3 * 2 * fakultaet(1)
= 4 * 3 * 2 * 1
= 24
"""

def fakultaet(n):
    if n == 1:
        return 1
    return n * fakultaet(n - 1)

print(fakultaet(4))  # Ergebnis: 120
