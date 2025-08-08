""" 
💡 Merksatz:
hier muss man eine zahl und keinen buchstaben eingeben,
falls ein buchstabe eingegeben wird, wird dieser abgefangen und eine Fehlermeldung ausgegeben.
"""

# ValueError: Falscher Wert / nicht umwandelbar
try:
    zahl = int(input("Gib eine Zahl ein: "))
    print("Deine Zahl ist:", zahl)
except ValueError:
    print("❌ Fehler: Das war keine gültige Zahl!")
