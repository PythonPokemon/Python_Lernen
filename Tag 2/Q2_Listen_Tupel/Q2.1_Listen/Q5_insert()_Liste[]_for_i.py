

def my_list(n):
    list = []
    for i in range(0,n):
        list.insert(0,i)    #  bei insert werden die elemente imme nach rechts verschoben
    return list
    
print(my_list(5))
