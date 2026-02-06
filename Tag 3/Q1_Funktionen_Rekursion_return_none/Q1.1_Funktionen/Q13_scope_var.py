# Namederror variable innerhalb der methode, nicht global
def my_function():
    var = 2
    print("zugriff und manipulation in der methode auf globale variable: ", var)

my_function()
print(var)