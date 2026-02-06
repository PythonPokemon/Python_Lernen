# dictionarys
dictionary = {"cat":"katze", "dog":"hund", "ape":"affe"}


# mit der .items() methode, als schlüsselwertpaar und verpackten tupels
print("----------------------------------------------------------------------")
for i in dictionary.items():
    print(i)


# mit der .items() methode, als schlüsselwertpaar und entspackten tupels
print("----------------------------------------------------------------------")
for schlüssel, wert in dictionary.items():
    print("einzelne ausgaben der schlüssel:--->", schlüssel, "<---und werte:--->", wert)

