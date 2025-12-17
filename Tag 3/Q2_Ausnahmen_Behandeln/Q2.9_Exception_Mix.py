"""
Versuch jetzt dein gelerntes wissen abzufragen indem du jede exception 1x triggerst

Lösung:

"""

try:
    print()

except ValueError:  
    print("❌ ValueError: Ungültiger Zahlenwert!")

except TypeError:
    print("❌ TypeError: Falsche Operation zwischen Datentypen!")

except ZeroDivisionError:
    print("❌ ZeroDivisionError: Durch Null darf man nicht teilen!")

except SyntaxError:
    print("❌ SyntaxError: Der Ausdruck enthält einen Schreibfehler!")

except Exception as e:
    print("⚠️ Ein anderer Fehler ist aufgetreten:", type(e).__name__)
