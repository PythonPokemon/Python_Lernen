# shadowing / überschattung von variablen gegenbeispiel
print("\n gegenbeispiel-shadowing\n")
param1 = 123456789
param2 = "aaaaaaaaaaaa"
param3 = 0.123

def message(param1, param2, param3):
    print("ein text und 3 params == ", param1, param2, param3)

message(1, 3.14, "string")
message(123, 456, 789)
message(1.1, 2.22, 3.333)
message("a", "bb", "ccc")


print(param1)
print(param2)
print(param3)