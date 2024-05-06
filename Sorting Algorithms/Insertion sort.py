# All items in the list must contain the same datatype

list = [2, 8, 5, 3, 9, 4]
main_index = 1

while main_index <= (len(list) - 1):
    temp_index = main_index

    while ((temp_index - 1) > -1):
        if list[temp_index] < list[temp_index - 1]:
            var1, var2 = list[temp_index], list[temp_index - 1]
            list[temp_index], list[temp_index - 1] = var2, var1
    
        temp_index = temp_index - 1
    
    main_index = main_index + 1

print(list)