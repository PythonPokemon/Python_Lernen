# oder list comprehansion mit variablen namen 
# als ausdruck
# der typ in der variable wird dann in die liste automatisch übernommen
variable = "abc"

my_list = [variable for i in range(0, 3)]

# exclusiv:-----------------------------
# inklsuvi:---------------             |
#                        |      |      |
#Index:                  0      1      2             
print(my_list)      # ['abc', 'abc', 'abc']
print(type(my_list))
