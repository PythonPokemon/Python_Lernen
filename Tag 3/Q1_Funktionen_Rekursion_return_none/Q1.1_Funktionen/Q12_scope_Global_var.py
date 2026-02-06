var = 1
print("bevor die globale variable in der methode ein neuer wert zugewiesen wurde:", var)

# global var
def my_function():
    global var
    var = 2
    print("zugriff und manipulation in der methode auf globale variable: ", var)



my_function()
print(var)