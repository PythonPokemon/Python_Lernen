# 'if', 'else', 'def', 'for', 'while', 'class', 'try', 'except', 'finally',
# 'return', 'import', 'from', 'as', 'with', 'lambda', 'and', 'or', 'not',
# 'in', 'is', 'pass', 'break', 'continue', 'yield', 'global', 'nonlocal',
# 'assert', 'del', 'raise', 'True', 'False', 'None' 

# -> das sind Beispiele für Python-Schlüsselwörter.

# and = 2   #keyword
true = 1
TRUE = 3
# True = 4  #keyword
FALSE = 5
false = 6
# False = 7 #keyword


print(true)
# print(and)
print(TRUE)
# print(True)
print(FALSE)
print(false)
# Print(False)
#------------------------------------------------------------------------------------------------


# WICHTIG: Einrückung ist in Python zwingend erforderlich, um Blöcke zu markieren.

alter = 18

if alter >= 18:                                 # 'if' ist ein Schlüsselwort -> Bedingung prüfen
    print("Du bist volljährig.\n")              # eingerückt -> gehört zum if-Block
else:                                           # 'else' ist ein Schlüsselwort -> Alternative
    print("Du bist noch nicht volljährig.\n")   # eingerückt -> gehört zum else-Block
