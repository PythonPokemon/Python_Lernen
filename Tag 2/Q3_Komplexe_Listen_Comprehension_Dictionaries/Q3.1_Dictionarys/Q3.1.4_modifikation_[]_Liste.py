
# dictionarys
dictionary = {"cat":"katze", "dog":"hund", "ape":"affe"}

# modifiezieren von werten
print(dictionary["ape"])                # ausgabe: vor der modfizierung!
dictionary["ape"] = "Monkey.D.Luffy"    # modifizierung
print(dictionary["ape"])                # ausgabe: nach der modifizierung!

# hinzufügen neuer paare: key:value
print(dictionary)                           # davor!
dictionary["Pirate King"] = "Gold.D.Roger"  #  key[] = value
print(dictionary)                           # danach


#--------------------------------------------------------------------------------------------------------