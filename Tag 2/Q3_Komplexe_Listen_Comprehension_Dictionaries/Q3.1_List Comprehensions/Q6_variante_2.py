# oder list comprehansion mit variablen namen 
# als ausdruck
# dieser typ wird dann übernommen
variable = "abc"

my_list = [variable for i in range(1, 3)]

print(my_list)
print(type(my_list))
