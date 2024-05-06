# l is the lowest index, h is the highest index
def Partition(array, l, h):
    pivot = array[l]
    left_index = l
    right_index = h
    
    while True:
        while left_index <= right_index and array[left_index] <= pivot:
            left_index += 1
        while right_index >= left_index and array[right_index] > pivot:
            right_index -= 1
        if left_index < right_index:
            array[left_index], array[right_index] = array[right_index], array[left_index]
        else:
            break
        
    array[l], array[right_index] = array[right_index], array[l]
    return right_index

def QuickSort(array, l, h):
    if l < h:
        j = Partition(array, l, h)
        QuickSort(array, l, j)
        QuickSort(array, j+1, h)
    
    return array

array = [10, 16, 8, 12, 15, 6, 3, 9, 5]
print(QuickSort(array, 0, len(array) - 1))

# Converted the algorithm used in the video below with few modifications
# https://www.youtube.com/watch?v=7h1s2SojIRw
# Checked and modified with the help of ChatGPT

# Note to self, 
# There is no need of a temporary variable when swapping in python