"""
String Verkettung

bsp. mit .input()
strings bei den der  + operator steht werden nicht addiert, sondern verkettet ---> hintereinander gecklebt
von links nach rechts!

"""

# bsp. der .input() befehl hat den standart rückgabewert string
# wenn man diesen nicht umwandelt in ein int bleibt es ein string

x = input('Gib deine erste Zahl ein: ')     # bsp. eingabe: 1
y = input('Gib deine zweite Zahl ein: ')     # bsp. eingabe: 3
print(x + y)    # Ergebnis 13 !