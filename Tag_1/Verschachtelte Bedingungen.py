# Bedingungen können ineinander verschachtelt werden

punktzahl = int(input("Wie viele Punkte hast du? "))

if punktzahl >= 50:
    print("Bestanden")
    
    if punktzahl >= 90:
        print("Mit Auszeichnung bestanden!")  # Diese Bedingung wird nur geprüft, wenn >= 50
else:
    print("Nicht bestanden")
