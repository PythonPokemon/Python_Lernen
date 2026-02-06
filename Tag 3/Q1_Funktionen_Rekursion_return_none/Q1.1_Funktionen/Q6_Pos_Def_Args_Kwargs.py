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

#-----------------------------------------------------------------------------------------------------------------------------
# nochmal mit anderen werten
def instrucktion(a, b=2, *args, **kwargs):
    print("positionalargument: ", a, "Default:", b, "beliebig viele args:", args, "beliebig viele kwargs:",  kwargs)

instrucktion(1, 3, 4, 4, x=10, y=200)
instrucktion(1.234, 0.99, 0.1, 0.2, x=0.987654321, y=999999999.999999999)
instrucktion('a', 'b', 'auch wörter als nur 1 arg', 'viele', 'viele argumente', xyz='keyargs')
instrucktion("aaaaa", "bbbbb", "ganz viele argumente", "noch mehr argumente", abcdefghijklmnopqrstuvwxyz=123456789, z=0.0001)
instrucktion(0.1, 9, 'abcdefg', "hijklmnop", qrstuvwxyz=0.1, gent=122333444455555666666777777788888888999999999)