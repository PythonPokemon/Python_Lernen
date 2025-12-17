"""
Versuch jetzt dein gelerntes wissen abzufragen indem du jede exception 1x triggerst

zum testen in den print() befehl einsetzten Lösung:
-------------------------------------------------------------------------------------
Fehlerklassen       | in den print  |               beschreibung                    |
-------------------------------------------------------------------------------------
ValueError:         |   int("abc")  |   "abc" kann nicht in int umgewandelt werden  |
-------------------------------------------------------------------------------------
TypeError:          |   5 + "abc"   |    Zahl + String = nicht erlaubt              |
 ------------------------------------------------------------------------------------
ZeroDivisionError:  |   10 / 0      |   Division durch Null nicht erlaubt           |
 ------------------------------------------------------------------------------------
SyntaxError:        | print(""      |   ungültiger Python-Ausdruck                  |
 ------------------------------------------------------------------------------------
Exception as e:     |
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
    print("❌ KeyError:")

except NameError:
    print("❌ NameError:")

except IndexError:
    print("❌ IndexError:")

except Exception as e:
    print("⚠️ Ein anderer Fehler ist aufgetreten:", type(e).__name__)
