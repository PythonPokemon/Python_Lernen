"""
Was bedeutet was und was hat priorität bei der initialisierung von Funktionen?

Keyword Arguments (kwargs) 
haben immer Priorität vor Positional Arguments (args), da sie explizit benannt werden. 
Wenn ein Argument sowohl als Positional Argument als auch als Keyword Argument übergeben wird, wird das Keyword Argument verwendet.

Arguments (args) 
sind die normalen Argumente, die in der Reihenfolge übergeben werden, wie sie definiert sind.

default_argument
 = 2 bedeutet, dass das Argument b einen Standardwert von 2 hat. 
Wenn die Funktion aufgerufen wird, ohne dass ein Wert für b angegeben wird, wird der Standardwert von 2 verwendet.

positional_arguments
 sind die Argumente, die in der Reihenfolge übergeben werden, wie sie definiert sind
...
"""


# krasser stuff
def beispiel(a, b=2, *args, **kwargs):
    print(a, b, args, kwargs)


beispiel(1, 2, 7, 8, 9, farbe="rot, gelb", zahl=3.14, y=15)