# shadowing / überschattung von variablen
param1 = 123456789
param2 = "aaaaaaaaaaaa"
param3 = 0.123

def message(param1, param2, param3):
    # variablen die innerhalb einer methode als parameter verwendet werden
    # werden mit den werten innerhalb der methode überschattet/verdeckt!
    param1 = 111
    param2 = 222
    param3 = "333"
    print("ein text und 3 params == ", param1, param2, param3)

message(param1=1, param2=2, param3=3)
message(123, 456, 789)


print(param1)
print(param2)
print(param3)