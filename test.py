my_list = [None, None, None]

my_list[0] = 1
my_list[1] = 2
my_list[2] = [3, [4, 5]]

print(my_list[2][0])        # 3
print(my_list[2][1])        # [4, 5]
print(my_list[2][-1])       # [4, 5]
print(my_list[-1][-1])      # [4, 5]
print(my_list[2][1][0])     # 4
print(my_list[2][1][1])     # 5
print(my_list[-1][1][1])    # 5
