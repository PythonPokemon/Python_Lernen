data = [4, 2, 3, 2, 1]
res = data[0]
 
for d in data:
    if d < res:
        res = d
 
print(res)