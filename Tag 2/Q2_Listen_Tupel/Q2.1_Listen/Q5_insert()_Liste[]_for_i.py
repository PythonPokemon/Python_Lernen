
def my_list(n):
    list = []
    for i in range(0,n):
        list.insert(0,i)
    return list
    
print(my_list(5))

x= my_list
print("\nSpeicheradresse der Funktion:", x)    # gibt die speicheradresse aus!
