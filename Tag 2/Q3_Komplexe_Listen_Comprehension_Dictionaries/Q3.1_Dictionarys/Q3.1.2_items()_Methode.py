# dictionarys
dictionary = {"cat":"katze", "dog":"hund", "ape":"affe"}


# Variante 1 | Ausgabe
# mit der .items() methode, als schlüsselwertpaar und verpackten tupels
print("----------------------------------------------------------------------")
for i in dictionary.items():
    print(i)


# Variante 2 | Ausgabe
# mit der .items() methode, als schlüsselwertpaar und entspackten tupels
print("----------------------------------------------------------------------")
for schluessel, wert in dictionary.items():
    print("Schlüssel:", schluessel, "| Wert:", wert)

