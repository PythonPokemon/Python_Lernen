"""
String Verkettung

mit casting und ohne casting
"""

print('ohne casting')
# ohne casting
x = input('Gib deine erste Zahl ein: ')     # bsp. eingabe: 1
y = input('Gib deine zweite Zahl ein: ')     # bsp. eingabe: 3
print(x + y)    # Ergebnis 13 !

print('------------------------------------------------------')

print('mit casting')
# mit casting | Der Datentyp string wird in eine Ganzzahl Int umgewandelt und die Werte werden tatsächlich operiert
x = int(input('Gib deine erste Zahl ein: '))     # bsp. eingabe: 1
y = int(input('Gib deine zweite Zahl ein: '))     # bsp. eingabe: 3
print(x + y)    # Ergebnis 4 !