# Testdatei für die Wiederholung von Themen
# Step-by-Step..

x = 1

x = x == x
print(x)

print("-----")

vals = [0, 1, 2]
vals.insert(0, 1)
print(vals)
del vals[1]
print(vals)

print("---------------------------------------------------------------")
#index    -4  -3 -2 -1
my_list = [1, 2, 3, 4]
print(my_list[-3:-2]) # 2

print("---------------------------------------------------------------")
z = 10
y = 0
x = y < z and z > y 

print(x)

print("---------------------------------------------------------------")
a = 1
b = 0

c = a & b   # and
d = a | b   # bitwise or
e = a ^ b   # XOR exclusiv or

print(c + d + e)    # 0 + 1 + 1

print("---------------------------------------------------------------")

z = y = x = 1
print(x, y, z, sep='*')