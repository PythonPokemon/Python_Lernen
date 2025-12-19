""" 
💡 Merksatz:
hier muss man eine zahl und keinen buchstaben eingeben,
falls ein buchstabe eingegeben wird, wird dieser abgefangen und eine Fehlermeldung ausgegeben..
"""

try:
    zahl = int(input("Gib eine zahl ein"))
    print("Deine zahl ist: ", zahl)
except ValueError:
    print(" Fehler das war keine gültige zahl!")