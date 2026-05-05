"""
.insert(startindex, wert) parameter angabe
bei .insert() werden die elemente imme nach rechts verschoben
"""

def my_list(n):
    list = [55, 77]
    for i in range(0,n):
        list.insert(1,i)    #  startindex == 1, hier werden die neuen werte insertet !
    return list
    
print(my_list(3))
