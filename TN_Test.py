my_dict={"bald":"Urlaub","Frohe":"Weihnachten","guten":"Rutsch"}

try:
    print(my_dict["bald"])
    print(my_dict["Urlaub"])
except KeyError:
    #freundlich:
    print("Du Pfeife machst heute aber ganz schön viele Fehler! Was soll das?")
    print("Fehler abgefangen: ein Key-Fehler!")
else:
    print("der Else-Block")