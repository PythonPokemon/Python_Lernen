"""
Notizen:
"""

dictionary = {"cat":"katze", "dog":"hund", "ape":"affe"}
print(dictionary,  " <--- dictionary, vor der änderung") 

dictionary.popitem()        # entfernt das letzte paar: Key/Value
print(dictionary,  " <--- dictionary, nach der änderung")

print(dictionary.popitem()) # print(popitem()) zeigt die werte an, die popitem entfernt hat




#--------------------------------------------------------------------------------------------------------
