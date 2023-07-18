# Insert(int[] sorted, int value)
#   initialize i to 0
#   WHILE value > sorted[i]
#     set i to i + 1
#   WHILE i < sorted.length
#     set temp to sorted[i]
#     set sorted[i] to value
#     set value to temp
#     set i to i + 1
#   append value to sorted

# InsertionSort(int[] input)
#   LET sorted = New Empty Array
#   sorted[0] = input[0]
#   FOR i from 1 up to input.length
#     Insert(sorted, input[i])
#   return sorted -->

# <!-- In your blog article, visually show the output of processing this input array:

int_array = [8, 4, 23, 42, 16, 15]

def insert(sorted_array, value):
    i = 0
    while i < len(sorted_array) and value > sorted_array[i]:
        i = i + 1
    sorted_array.insert(i, value)

def insertion_sort(input_array):
    sorted_array = [input_array[0]]
    for i in range(1, len(input_array)):
        insert(sorted_array, input_array[i])
    return sorted_array

# Test the insertion_sort function with the given input array [8, 4, 23, 42, 16, 15]
input_array = [8, 4, 23, 42, 16, 15]
sorted_array = insertion_sort(input_array)
print(sorted_array)



# In order to run command
# Inside of sorting folder
# python3 -m insertion.test_insertion
# Having a tests folder caused code to not being able to find sort folder
