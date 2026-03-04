
"""
🧠 Python-Scope-Regel (LEGB-Regel)

Python sucht Variablen in dieser Reihenfolge:
1.Local (innerhalb der Funktion)
2.Enclosing (äußere Funktion, bei verschachtelten Funktionen)
3.Global (Modulebene)
4.Built-in

In deinem Fall:
Lokal → gibt es kein var
Enclosing → gibt es nicht
Global → var = 1 gefunden ✔
"""

var = 1
print("bevor die globale variable in der methode ein neuer wert zugewiesen wurde:", var)

# global var
def my_function():
    global var
    var = 2
    print("zugriff und manipulation in der methode auf globale variable: ", var)


print(var)
my_function()
print(var)