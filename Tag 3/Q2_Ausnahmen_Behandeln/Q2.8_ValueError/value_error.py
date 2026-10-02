""" 
💡 Merksatz:
ValueError findet statt, wenn der Datentyp zwar korrekt ist aber ein falscher wert übergeben wird,
bsp. int wird erwartet, aber man gibt einen buchastaben ein a obwohl der datentyp int ist!
hier muss man eine zahl und keinen buchstaben eingeben,
falls ein buchstabe eingegeben wird, wird dieser abgefangen und eine Fehlermeldung ausgegeben..
"""

try:
    zahl = int(input("Gib eine zahl ein: "))
    print("Deine zahl ist: ", zahl)
except ValueError:
    print(" Fehler das war keine gültige zahl!")