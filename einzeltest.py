# index;   0  1  2
# count 3
my_list = [9, 7, 8]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)