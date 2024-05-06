list = [9, 1, 8, 2, 7, 3, 6, 4, 5]

min_index = 0
cur_index = 0

for i in range(len(list)):
    current_minimum = list[min_index]
    original_minimum = list[min_index]

    while cur_index < len(list) - 1:
        cur_index = cur_index + 1
        current_item = list[cur_index]

        if current_minimum > current_item:
            current_minimum = current_item
            save_cur_index = cur_index
                
    var1, var2 = original_minimum, list[save_cur_index]
    list[min_index], list[save_cur_index] = var2, var1
    
    min_index = min_index + 1
    cur_index = min_index

print(list)