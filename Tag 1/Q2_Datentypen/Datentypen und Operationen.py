# 🧠 Python-Datentypen, Objekttypen & Typ-Umwandlungen – Übersicht & Beispiele

# --- Datentypen ---
ganzzahl = 42                   # int – ganze Zahl
kommazahl = 3.14                # float – Kommazahl
komplexe_zahl = 2 + 3j          # complex – komplexe Zahl mit Real- und Imaginärteil
text = "Hallo Welt"             # str – Zeichenkette
wahrheitswert1 = True           # bool – Wahr
wahrheitswert2 = False          # bool - Falsch
liste = [1, 2, 3]               # list – veränderbare Liste
tupel = (4, 5, 6)               # tuple – unveränderbare Liste
menge = {1, 2, 3}               # set – Menge ohne Duplikate
dictionary = {"a": 1, "b": 2}   # dict – Schlüssel/Wert-Paare
nichts = None                   # NoneType – "kein Wert"

# --- Objekttypen anzeigen ---
print(type(ganzzahl))           # <class 'int'>
print(type(kommazahl))          # <class 'float'>
print(type(komplexe_zahl))      # <class 'complex'>
print(type(text))               # <class 'str'>
print(type(wahrheitswert1))     # <class 'bool'>
print(type(liste))              # <class 'list'>
print(type(tupel))              # <class 'tuple'>
print(type(menge))              # <class 'set'>
print(type(dictionary))         # <class 'dict'>
print(type(nichts))             # <class 'NoneType'>

# --- Typ-Umwandlungen (Casting) ---
# int()    → in Ganzzahl umwandeln
# float()  → in Kommazahl umwandeln
# complex()→ in komplexe Zahl umwandeln
# str()    → in Zeichenkette umwandeln
# bool()   → in Wahr/Falsch umwandeln
# list()   → in Liste umwandeln
# tuple()  → in Tupel umwandeln
# set()    → in Menge umwandeln
# dict()   → in Dictionary umwandeln (aus z.B. Tupel-Liste)

# Beispiele:
print(int(3.99))                # 3
print(float("5.67"))            # 5.67
print(complex(2, 5))            # (2+5j)
print(str(123))                 # "123"
print(bool(0))                  # False
print(list((1, 2, 3)))          # [1, 2, 3]
print(tuple([4, 5, 6]))         # (4, 5, 6)
print(set([1, 2, 2, 3]))        # {1, 2, 3}
print(dict([("x", 10), ("y", 20)]))  # {'x': 10, 'y': 20}
