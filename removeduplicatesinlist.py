list = [5,6,4,2,5,6,2]
for i in list:
    if list.count(i)>1:
        list.remove(i)
list.sort()
print(list)