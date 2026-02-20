# 'if', 'else', 'def', 'for', 'while', 'class', 'try', 'except', 'finally',
# 'return', 'import', 'from', 'as', 'with', 'lambda', 'and', 'or', 'not',
# 'in', 'is', 'pass', 'break', 'continue', 'yield', 'global', 'nonlocal',
# 'assert', 'del', 'raise', 'True', 'False', 'None' 

# -> das sind Beispiele für Python-Schlüsselwörter.



# else wird immer ausgeführt hier
for i in range(1):
    print("#")
else:
    print("#")

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
# keyword 'in' that's why Syntaxerror
# try insteat with 'it'

# def fun(in=2, out=3):
#     return in * out

# print(fun(3))
#--------------------------------------------------------------------------------------------------------

def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return
    
print(fun(fun(2)) +1)   # +1 erzeugt TypeError
#--------------------------------------------------------------------------------------------------------
def fun(inp=2, out=3):
    return inp * out

print(fun(out=2))   # man darf 1x kwargs stehen lassen, aber nicht kwargs, pos
#--------------------------------------------------------------------------------------------------------
def f(x):
    if x == 0:
        return 0
    return x + f (x -1)

print(f(3))

"""
f(3) == 6
f(2) == 3
f(1) == 1
"""
#--------------------------------------------------------------------------------------------------------

my_list = ['Mary', 'had', 'a', 'little', 'lamb']


def my_list(my_list):
    del my_list[3]
    my_list[3] = 'ram'

print(my_list(my_list)) # try it so: print(my_list)

"""
1️⃣ Problem: Name-Kollision

Du hast zwei Dinge mit demselben Namen my_list:

my_list ist zuerst eine Liste, Danach definierst du my_list als Funktion
Python überschreibt dann die Liste durch die Funktion. 
Ab dem Moment der Funktionsdefinition ist my_list nicht mehr die Liste, 
sondern die Funktion.
"""
#--------------------------------------------------------------------------------------------------------
foo = (1, 2, 3)

foo.index(1) # output 1
foo.index(0) # valueError

# foo.index[0] TypeError
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
x = 3
y = 2

x = x % y
x = x % y
y = y & x
print(y)
#--------------------------------------------------------------------------------------------------------
my_list = [ x * x for x in range(5)]

def fun(lst):
    del lst[lst[2]]
    return lst

print(fun(my_list))
#--------------------------------------------------------------------------------------------------------
"""
✅ Summe der Fehler: 5 Fehler

break außerhalb einer Schleife → SyntaxError
except: vor spezifischem except block → SyntaxError
Unerreichbarer except Block → SyntaxError
Code hinter print(5/0) wird nie ausgeführt → logischer Fehler
ZeroDivisionError wird nicht spezifisch behandelt → logischer Fehler
"""

# try:
#     print(5/0)
#     break
# except:
#     print("Sorry, something went wrong")
# except (ValueError, ZeroDivisionError):
#     print("Too bad...")

#--------------------------------------------------------------------------------------------------------

my_list = [1, 2]

for v in range(2):
    my_list.insert(-1,my_list[v])

print(my_list)
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
# die variable 'ch' soll nicht 'in' hi nach charakert suchen...
# sondern das ist nur eine irreführung!
# iat normale for i in range()
for ch in "hi":
    print(ch)

#--------------------------------------------------------------------------------------------------------
x = 1
y = 1.0
z = "1"

if x == y:
    print("one")

if y == int(z):
    print("two")

# elif wird nur ausgeführt wenn das if darüber nicht true ist!
elif x == y:     
    print("three")

# else/sonst wird nur ausgeführt wenn alles davor false war!
else:
    print("four")

#--------------------------------------------------------------------------------------------------------
# kommentar
try:
    value = input("Enter a value: ")
    print(value/value)
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")
#--------------------------------------------------------------------------------------------------------
# ✅ ❌
