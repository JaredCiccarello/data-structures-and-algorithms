def mergesort(arr):
    n = len(arr)

    if n > 1:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)  # sort the left side
        mergesort(right)  # sort the right side

        merge(left, right, arr)  # merge the sorted left and right sides together

def merge(left, right, arr):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy remaining elements from left array, if any
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy remaining elements from right array, if any
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
