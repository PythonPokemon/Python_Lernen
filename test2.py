# iteratives Mapping
#index          0               1            2
dictionary = {'one': 'two', 'three':'one', 'two':'three'}   # länge:3
v = dictionary['one']

for k in range (len(dictionary)):
    v = dictionary[v]

print(v)
print(k)
print(dictionary)
