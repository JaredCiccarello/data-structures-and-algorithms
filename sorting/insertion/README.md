# Blog Notes: Insertion Sort
Merge Sort!

What is it? Put simply, it's a sorting algorithm, that divides an array in smaller arrays until it can no longer be divided. It then sorts each subarray and merges them back together to form a sorted array.

This algorithm is considered recursive because it continously splits until it can divide no further.

How does it work? I'm glad you asked!

First we want to document our space and time complexity.
Space: O(n)
Time: O(n)

Next we identify our array.

Now we can get started with our algorithm.
We start by writing a function of MergeSort, passing in the arr or array for short.

We declare a variable of n to be the arr.length or the length of the array. n = arr.length

Here we set a condition, if n > 1. Here we are saying that if n is greater than 1 do something.

In this case, if n is greater than 1 we want it to DECLARE. Declare in this case is a placeholder as a way to indicate the creation of variables.

We assign the middle of array to be n/2
Left is 0 to mid
Right is mid to n

Here we are assigning the different sections of our array and then sorting them.

First we sort left, then right, and then merge them together using left, right, arr.

We declare individual variables for i, j, and k to help create our next while loop.

Inside of our while loop we define our variables where i less than the left.length and j is less than the right.length.

After assigning the value to the merged array, k is incremented by 1 to move to the next position in the merged array.

Once the while loop finishes, it means either the left or the right array has been completely processed. If i has reached the length of the left array, it means all elements from the left array have been merged into the merged array. In this case, the remaining elements in the right array are appended to the merged array (arr).

Conversely, if i is not equal to the length of the left array, it means all elements from the right array have been merged, and the remaining elements in the left array are appended to the merged array (arr).

Finally, the Merge function completes, and the merged array (arr) is returned.


  Visual:
We start with our array
[8,4,23,42,16,15]
This array length is greater than 1.
We declare the mid index at n/2

[8,4,23] [42,16,15]

[8,4,23]

This array is still greater than 1.

[8] [4,23]

[4,23]
This array is sorted further into
[4] and [23]

This subarray is then merged.

[4, 23]


 [42,16,15]

This array is still greater than 1.

[42] [16,15]

[16,15]
This array is sorted further into
[16] and [15]

This subarray is then merged.
[16, 15]

Then both subarrays are merged and sorted

[4, 8, 15, 16, 23, 42]
