""" 
Vergleich von Zeichenketten

Beachte: Zeichenketten werden zeichenweise verglichen, nicht numerisch!
bsp.
'A' == 65
'a' == 97
-----------------------------------------------------------------------
Merksatz: 
einfach alphabetisch hochzählen von startwert bis endwert:

'A' == 65 bis 'Z' == 90
'a' == 97 bis 'z' == 122
"""


print("Apfel" == "Apfel")   # True. da beides zeichenketten sind und gleich
print("Apfel" < "Banane")   # True 'ACHTUNG'!, da alphabetisch sind!| vergleicht nur ersten string | A == 65 < B == 66
print("10" < "2")           # True (Zeichenvergleich, nicht als Zahl!)
print("1" == 1)             # False (Typen sind unterschiedlich: String vs. Integer)



# UNICODE / ASCII-Zeichen Codierung Beispiel!
print("------")
print(ord("A"))             # 65
print(ord('Z'))             # 66

print(chr(65))              # 'A'
print(chr(66))              # 'B'