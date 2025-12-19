



try:
    # Code, der Fehler machen kann
    print(19/0)
except (TypeError, ValueError, ZeroDivisionError, AttributeError):
    print("Einer dieser Fehler ist passiert.")