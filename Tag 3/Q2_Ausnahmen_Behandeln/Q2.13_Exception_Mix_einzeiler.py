



try:
    # Code, der Fehler machen kann
    print(1+"a")
    print(19/0)
except (TypeError, ValueError, ZeroDivisionError, AttributeError): # standart Edube
    print("Einer dieser Fehler wurde ausgelöst.")
finally:
    print("kjnliuh")