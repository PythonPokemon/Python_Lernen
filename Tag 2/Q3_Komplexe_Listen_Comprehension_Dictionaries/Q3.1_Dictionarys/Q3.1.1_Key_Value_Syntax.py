# dictionarys
dictionary = {"cat":"katze", "dog":"hund", "ape":"affe"}

# standart abfrage
for i in dictionary.keys():
    print("Zeige den schlüssel:-->", i, "<---und den wert:--->", dictionary[i])

# mit der .items() methode, als schlüsselwertpaar und verpackten tupels
print("----------------------------------------------------------------------")
for i in dictionary.items():
    print(i)

# mit der .items() methode, als schlüsselwertpaar und entspackten tupels
print("----------------------------------------------------------------------")
for schlüssel, wert in dictionary.items():
    print("einzelne ausgaben der schlüssel:--->", schlüssel, "<---und werte:--->", wert)

"""
das ist equivalenz dazu:
paar = ("x", "y")
a, b = paar  # Entpacken

print(a)  # x
print(b)  # y
"""

# mit der .values() methode gibt man nur werte aus, keine schlüssel!
print("----------------------------------------------------------------------")
for i in dictionary.values():
    print("ausgabe der werte:", i)
#--------------------------------------------------------------------------------------------------------
# dictionarys
dictionary = {"cat":"katze", "dog":"hund", "ape":"affe"}

# modifiezieren von werten
print(dictionary["ape"])    # vor der modfizierung!
dictionary["ape"] = "Monkey.D.Luffy"
print(dictionary["ape"])    # nach der modifizierung!

# hinzufügen neuer paare: key:value
print(dictionary)           # davor!
dictionary["Pirate King"] = "Gold.D.Roger" #  key[] = value
print(dictionary)           # danach

# oder hinzufügen über .update() methode
dictionary.update({"Hokage":"Naruto"})
print(dictionary)

# removing keys | löscht auch automatisch die werte
del dictionary["Hokage"]
print(dictionary)

#--------------------------------------------------------------------------------------------------------
# dictionarys
dictionary = {"cat":"katze", "dog":"hund", "ape":"affe"}

print(dictionary) # bevor das letzte paar entfernt wird!
dictionary.popitem()
print(dictionary)   # nachdem entfern des letzten key:value pair
#--------------------------------------------------------------------------------------------------------