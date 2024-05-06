# List must contain the same datatype

list = []

for x in range(len(list)):
    index = 0
    while (index + 1) < len(list):
        if list[index] > list[index + 1]:
            var1, var2 = list[index], list[index + 1]
            list[index], list[index + 1] = var2, var1
        
        index = index + 1

print(list)
