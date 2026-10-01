"""
Merke:
---------------------------------------------------------------------------------------------------------
popitem() → entfernt das letzte eingefügte Paar und gibt es zurück.
Ist das Dictionary leer, löst popitem() einen KeyError aus.
---------------------------------------------------------------------------------------------------------
Notizen:
"""

dictionary = {"cat":"katze", "dog":"hund", "ape":"affe"}
print(dictionary,  " <--- dictionary, vor der änderung") 

dictionary.popitem()        # entfernt das letzte paar: Key/Value
print(dictionary,  " <--- dictionary, nach der änderung")





#--------------------------------------------------------------------------------------------------------
