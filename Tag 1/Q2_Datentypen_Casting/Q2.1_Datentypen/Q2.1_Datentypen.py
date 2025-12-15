# 🧠 Python-Datentypen, Objekttypen & Typ-Umwandlungen – Übersicht & Beispiele

# --- Datentypen ---
ganzzahl = 42                   # int – ganze Zahl
kommazahl = 3.14                # float – Kommazahl
komplexe_zahl = 2 + 3j          # complex – komplexe Zahl mit Real- und Imaginärteil
text = "Hallo Welt"             # str – Zeichenkette
wahrheitswert1 = True           # bool – Wahr
wahrheitswert2 = False          # bool - Falsch
liste = [1, 2, 3]               # list –  geordnete Sequenzen | veränderbare Liste
tupel = (4, 5, 6)               # tuple – geordnete Sequenzen | unveränderbare Liste
menge = {1, 2, 3}               # set – Menge ohne Duplikate
dictionary = {"a": 1, "b": 2}   # dict – Schlüssel/Wert-Paare
nichts = None                   # NoneType – "kein Wert"

# --- Objekttypen anzeigen ---
print(type(ganzzahl))           # <class 'int'>
print(type(kommazahl))          # <class 'float'>
print(type(komplexe_zahl))      # <class 'complex'>
print(type(text))               # <class 'str'>
print(type(wahrheitswert1))     # <class 'bool'>
print(type(wahrheitswert2))     # <class 'bool'>
print(type(liste))              # <class 'list'>
print(type(tupel))              # <class 'tuple'>
print(type(menge))              # <class 'set'>
print(type(dictionary))         # <class 'dict'>
print(type(nichts))             # <class 'NoneType'>
print("\n")                     # zeilenumbruch

# teste das!
print("ab hier beginnt die Praxis:-)")

irgendeineZahl = 12344
print(type(irgendeineZahl))
