""" 
Vergleich von Zeichenketten

Beachte: Zeichenketten werden zeichenweise verglichen, nicht numerisch!
"""


print("Apfel" == "Apfel")   # True
print("Apfel" < "Banane")   # True (alphabetisch)
print("10" < "2")           # True (Zeichenvergleich, nicht als Zahl!)
print("1" == 1)             # False (Typen sind unterschiedlich: String vs. Integer)