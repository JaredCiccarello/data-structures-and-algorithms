import pytest
from merge import mergesort

def test_mergesort_empty():
    arr = []
    mergesort(arr)
    print(arr)
    # Output: []

# Run the empty array test
test_mergesort_empty()

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

def test_mergesort_1():
    arr = [8, 4, 23, 42, 16, 15]
    mergesort(arr)
    print(arr)
    # Output: [4, 8, 15, 16, 23, 42]

def test_mergesort_2():
    arr = [5, 2, 9, 1, 7]
    mergesort(arr)
    print(arr)
    # Output: [1, 2, 5, 7, 9]

# Run the individual test functions
test_mergesort_1()
test_mergesort_2()
