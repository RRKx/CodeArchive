def StalinSort(numbers_list):

    if numbers_list:
        current_number = 0

        for number in numbers_list:
            if number > current_number:
                current_number = number
            else:
                numbers_list.remove(number)
        
        return f"Sorted list: {numbers_list}"
    else:
        return "List is empty"

numbers_list = []
print(StalinSort(numbers_list))