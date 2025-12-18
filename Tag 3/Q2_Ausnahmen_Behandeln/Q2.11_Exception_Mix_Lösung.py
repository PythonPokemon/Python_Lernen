"""
Versuch jetzt dein gelerntes wissen abzufragen indem du jede exception 1x triggerst
die beschreibungen sind teilweise kontextbezogen zu dieser aufgabe!

zum testen in den print() befehl einsetzten Lösung:
-------------------------------------------------------------------------------------
Fehlerklassen       |   im print()  |               beschreibung                    |
-------------------------------------------------------------------------------------
ValueError:         |   int("abc")  |   "abc" kann nicht in int umgewandelt werden  |
-------------------------------------------------------------------------------------
TypeError:          |   5 + "abc"   |   Zahl + String = nicht erlaubt               |
-------------------------------------------------------------------------------------
ZeroDivisionError:  |   10 / 0      |   Division durch Null nicht erlaubt           |
-------------------------------------------------------------------------------------
SyntaxError:        | print(""      |   ungültiger Python-Ausdruck                  |
-------------------------------------------------------------------------------------
AttributeError:     | var.append()  |   bei ungültigem functions aufruf             |
-------------------------------------------------------------------------------------
KeyError:           | dictionary[3] |   key existiert nicht, sondern [1] und [2]    |
-------------------------------------------------------------------------------------
NameError:          |      var      |    die variable existiert nicht               |
-------------------------------------------------------------------------------------
IndexError:         |   liste[5]    |   index 5 existiert nicht, nur: 0...4         |
-------------------------------------------------------------------------------------
ImportError:        |   import aaa  |   Modul konnte nicht importiert werden        |
-------------------------------------------------------------------------------------
Exception as e:     | keine speziele|   wenn eine spezielle klasse fehlt!           |
-------------------------------------------------------------------------------------
"""
#import aaa


dictionary = { 1 : "eins", 2 : 3 }
liste = [1, 2, 3, 4, 5]
var = "variable"


try:
    print()    # hier testen:-)

except ValueError:
    print("❌ ValueError: Ungültiger Zahlenwert!")

except TypeError:
    print("❌ TypeError: Falsche Operation zwischen Datentypen!")

except ZeroDivisionError:
    print("❌ ZeroDivisionError: Durch Null darf man nicht teilen!")

except SyntaxError:
    print("❌ SyntaxError: Der Ausdruck enthält einen Schreibfehler!")

except AttributeError:
    print("❌ AttributeError:")

except KeyError:
    print("❌ KeyError: key existiert nicht, sondern [1] oder [2]")

except NameError:
     print("❌ NameError: die variable existiert nicht == evtl. hier ausgegraut!")

except IndexError:
    print("❌ IndexError: index 5 existiert nicht, die Indizes sind jeweils von: 0...4")

except ImportError:
    print("❌ Fehler: Dieses Modul konnte nicht importiert werden!")

except Exception as e:
    print("⚠️  Allgemeine Fehlerbehandlung: Ein anderer Fehler ist aufgetreten, der hier nicht definiert wurde:", type(e).__name__)
