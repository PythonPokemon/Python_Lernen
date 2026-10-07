# Einfach jeweils auskommentieren zum testen der AUfgaben!

# # Testdatei für die Wiederholung von Themen
# # Step-by-Step..
# ----------------------------------------------------------
# x = 1

# x = x == x
# print(x)

# print("-----")

# vals = [0, 1, 2]
# vals.insert(0, 1)
# print(vals)             # Ausgabe?
# del vals[1]
# print(vals)             # Ausgabe?

# print("---------------------------------------------------------------")
# #index    -4 -3 -2 -1
# my_list = [1, 2, 3, 4]
# print(my_list[-4:-1])   # Ausgabe?

# print("---------------------------------------------------------------")
# z = 10
# y = 0
# x = y < z and z > y 

# print(x)                # Ausgabe?

# print("---------------------------------------------------------------")
# a = 1
# b = 0

# c = a & b   # and
# d = a | b   # bitwise or
# e = a ^ b   # XOR exclusiv or

# print(c + d + e)        # Ausgabe?

# print("---------------------------------------------------------------")

# z = y = x = 1
# print(x, y, z, sep='*') # Ausgabe?

# print("---------------------------------------------------------------")

# variable = 1, 2, 3, 456, 8888, 1.12, [12], {1333}, ("hgv")

# print(variable)         # Ausgabe?

# print("---------------------------------------------------------------, Modul 3 Quiz")
# #index revevrse
# #         -3  -2  -1
# my_list = [3, 1, -1]
# my_list[-1] = my_list[-2]   # der wert -2 ist 1 und dieser wird der liste übergeben und diese setzt ihn wider auf einen neuen index
# print(my_list)          # Ausgabe?

# print("---------------------------------------------------------------")

# nums = []
# vals = nums

# vals.append(1)
# print(nums)         # Ausgabe?
# print(vals)         # Ausgabe?
# print(nums == vals) # werte gleich?
# print(nums is vals) # adresse gleich? | Referenz zum gleichen objekt?
# print(id(nums))     # Ausgabe?
# print(id(vals))     # Ausgabe?

# print("---------------------------------------------------------------")
# nums2 = []
# vals2 = nums2[:]

# vals2.append(1)
# print(nums2)
# print(vals2)
# print(nums2 == vals2) # werte gleich?
# print(nums2 is vals2) # adresse gleich? | Referenz zum gleichen objekt?
# print(id(nums2))
# print(id(vals2))

# print("---------------------------------------------------------------")

# my_list3 = [0 for i in range(1, 3)] # inkl: 1, excl: 3
# print(my_list3)                     # Ausgabe?

# print("---------------------------------------------------------------")

# my_list4 = [0, 1, 2, 3]
# x = 1
# for element in my_list4:
#     x *= element
# print(x)                            # Ausgabe?

# print("--------------------------------------------------------------- Modultest 3")

# var5 = 0
# while var5 < 6:
#     var5 += 1
#     if var5 % 2 == 0:
#         continue
#     print("#")                      # Ausgabe?

# print("---------------------------------------------------------------")

# nums6 = [1, 2, 3]
# vals6 = nums6 [-1:-2]

# print(vals6)                        # Ausgabe?

# print("---------------------------------------------------------------")

# for i in range(1):                  # 1 ist exclusiv
#     print("#")
# else:
#     print("#")                      # Ausgabe?

# print("---------------------------------------------------------------")

# my_list7 = [[0, 1, 2, 3] for i in range (2)]    #  ist exclusiv
# print(my_list7[1][0])               # Ausgabe?

# print("---------------------------------------------------------------")
# print("kompliziert")
# my_list8 = [1, 2, 3]

# for v in range (len(my_list8)):     # range(3)
#     my_list8.insert(1, my_list8[v])
# print(len(my_list8))                # Ausgabe?

# print("---------------------------------------------------------------")

# my_list9 = [1, 2, 3]
# my_list10 = []

# for v in my_list9:
#     my_list10.insert(0, v)
# print(my_list10)            # insert schiebt die elemente nach rechts!
#                             # Ausgabe?
# print("---------------------------------------------------------------")

# dd = {"1": "0", "0": "1"}

# for x in dd.values():
#     print(x, end="")        # Ausgabe?

# print("---------------------------------------------------------------")

# #Index Reverse

# # start------------
# # ende----------  |
# #              |  |
# #         -3  -2 -1
# liste20 = [1, 2, 3,]
# x21 = liste20[-1:-2]

# print(x21)                  # Ausgabe?

# print("---------------------------------------------------------------Modultest 4")

# def fun(a=2, out=4):
#     return a * out

# print(fun(3))               # Ausgabe?

# print("---------------------------------------------------------------")

# tup = (1,) + (1,)
# tup = tup + tup
# print(len(tup))             # Ausgabe?

# print("---------------------------------------------------------------")

# def func(a, b):             # Achtung methodensignatur beachten!
#     return a ** b

# #print(func(2))             # Ausgabe?

# print("---------------------------------------------------------------")

# def fun(x):
#     if x % 2 == 0:
#         return 1        # erzeugt wenn true | Ausgabe: 1
#     else:
#         return          # erzeugt wenn false | Ausgabe: None

    
# # print(fun(fun(2)) +1)   # deshalb TypeError: None + 1  geht nicht!


# print("---------------------------------------------------------------")
# """
# Python-Scope-Regel (LEGB-Regel)

# Python sucht Variablen in dieser Reihenfolge:
# 1.Local (innerhalb der Funktion)
# 2.Enclosing (äußere Funktion, bei verschachtelten Funktionen)
# 3.Global (Modulebene)
# 4.Built-in

# In deinem Fall:
# Lokal → gibt es kein var
# Enclosing → gibt es nicht
# Global → var = 1 gefunden ✔
# """
# def any():
#     print(var +1, end='')

# var=1
# print(var)              # Ausgabe?
# any()                   # Ausgabe?
# print(var)              # Ausgabe?


# print("---------------------------------------------------------------")

# # iteratives Mapping
# #index          0               1            2
# dictionary = {'one': 'two', 'three':'one', 'two':'three'}   # länge:3
# v = dictionary['one']

# for k in range (len(dictionary)):
#     v = dictionary[v]

# print(v)

# print("---------------------------------------------------------------")

# def fun(x, y, z):
#     return x + 2 * y + 3 * z

# print( fun(0, z=1, y=3))    # Ausgabe?

# print("---------------------------------------------------------------")

# """
# In der ersten Schleife wird ein Dictionary aufgebaut, das die Schlüssel 'a', 'b', 'c' 
# jeweils auf ein 1-Element-Tupel wie ('a',) abbildet (das -1 sorgt dafür, dass 'd' nicht mitkommt).

# In der zweiten Schleife wird über die sortierten Schlüssel iteriert und der jeweilige Tupel-Wert in k gespeichert.
# Da k ein Tupel ist, muss man mit k[0] auf das enthaltene Zeichen zugreifen, um nur a, b, c auszugeben.
# """

# dictionary = {}
# my_list = ['a', 'b', 'c', 'd']

# for i in range(len(my_list) - 1):   # exclusiv
#     dictionary[my_list[i]] = (my_list[i], )

# #print(dictionary)   #{'a': ('a',), 'b': ('b',), 'c': ('c',)}

# for i in sorted(dictionary.keys()):
#     k = dictionary[i]
#     # Insert your code here
#     print(k[0])     # gibt untereinander aus: abc                   == entpackte tupel werte
#     #print(k)        # gibt untereinander aus: ('a',)('b',)('c',)   == verpackte tupel werte
#     #print(k["0"])   # TypeError
#     #print(k['0'])   # TypeError

# print("--------------------------------------------------------------- ab hier neue!")

# foo = (1, 2, 3)

# foo.index(1) # output 1
# # foo.index(0) # valueError

# print(foo.index(0))

# print("---------------------------------------------------------------")

# nums = [1, 2, 3]
# vals = nums
# del vals[:]

# print(nums)
# print(vals)

# print("---------------------------------------------------------------")

# lst = [ i for i in range (-1, -2)]

# print(lst)  # Ausgabe

# print("---------------------------------------------------------------")

# def func(a, b):
#     return b **a

# print(func(b=2, 2)) # Ausgabe

# print("---------------------------------------------------------------")

# """
# die erste schleife :
# for i in range (4) # sagt das die liste nur 4 elemente enthalten soll: [3, 3, 3, 3]
# angefangen mit 4-1 == 3

# die zweite schleife :
# for j in range (5) # sagt das 5 listen innerhalb der liste erzeugt werden sollen [3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3]
# """
# #Anzahl listen: 5 []                                             |              |             |             |             |
# #Anzahl elemente in der list: 4                             |  |  |  |
# #      :      4                   5
# t = [[4-1 for i in range (4)] for j in range (5)]   # t = [[3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3]]
# s = 0
# for i in range(3):  # schleife läuft 3x von 0, 1, 2 bis 3 exclusiv
#     s += t[i][i]    # wird jeweils um das äußere i == 3 und das innere j == 3 dazu addiert und in s überschrieben
# print(s)

# print("---------------------------------------------------------------")



# print("---------------------------------------------------------------")

# print("---------------------------------------------------------------")

# print("---------------------------------------------------------------")

# print("---------------------------------------------------------------")

# print("---------------------------------------------------------------")

