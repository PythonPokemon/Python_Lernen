"""
Versuch jetzt dein gelerntes wissen abzufragen indem du jede exception 1x triggerst
schreibe deine notizen bei den lösungen auf :-)
-----------------------------------------------------------------------------------
Lösung:

-----------------------------------------------------------------------------------
"""

try:
    print(10/0)    # hier testen:-)

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

except BaseException as e:
    print("⚠️  Allgemeine Fehlerbehandlung: Ein anderer Fehler ist aufgetreten, der hier nicht definiert wurde:", type(e).__name__)
finally:
    print("|-> und ich werde einfach immer ausgeführt, egal ob ein fehler passiert oder nicht!")
