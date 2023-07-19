# Blog Notes: Insertion Sort

<!-- https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-05/resources/singly_linked_list.html
Linked List article is a good example -->

<!-- [8,4,23,42,16,15] -->

This is what insertionSort is, and why it's important to use this method.


Big O
time: O(n)
space:O(1)


So how does the algorithm work?

For the Insert

Step 1
You have an internal 'insert' method being used to push data into your int array, which is also using a method to sort the information.

Step2
You have an int short for integer value which takes in a value and is then manipulated.

Step3
You start with your i, which is being set to 0 so that your i has a basic value.

Step4
Then take your while loop so that your function is being iterated over multiple times.

Step5
Next we create our value > sorted[i] which means the value must be greater than the sorted i value.

Step6
We want our i value to continue to increase by + 1

Step7
Next, we are using a for loop to find if your i value is less than the sorted value.length, meaning if the length of the integers have no values that are greater than the i value. Once we exit the loop we append to the end of the sorted array.


For the InsertionSort

Step 1
The code begins by defining a function named "InsertionSort" that takes an input array as a parameter. It also initializes a new empty array called "sorted" to store the sorted elements.

Step 2
The first element of the input array (input[0]) is assigned to the first position in the sorted array (sorted[0]). This is because a single element is always considered sorted.

Step 3
The code enters a loop that starts from the second element of the input array (input[1]) and iterates up to the length of the input array.

Step 4
Inside the loop, the "Insert" function is called, passing in the sorted array and the current element of the input array (input[i]). This function is responsible for inserting the current element into its correct position in the sorted array.

Step 5
The Insert function is not explicitly defined in the given code, but it is assumed to be a separate function that performs the insertion operation. The purpose of this function is to find the correct position in the sorted array to insert the current element. It shifts elements in the sorted array to the right until it finds the appropriate position for insertion.

Step 6
To find the correct position, the Insert function compares the current element with each element in the sorted array from right to left. If an element in the sorted array is greater than the current element, it is shifted one position to the right to make space for the insertion.

Step 7
Once the correct position is found, the current element is inserted into the sorted array at the appropriate index.

Step 8
The loop continues until all elements in the input array have been processed and inserted into the sorted array.

Step 9
After the loop completes, the function returns the sorted array.



Let's do a stepthrough of this code.

This is the array
[8, 4, 23, 42, 16, 15]

This is the array sorted
[4, 8, 15, 16, 23, 42]


We take 8 and iterate through it.

First iteration

Next we take the next value of 4 and compare. [8, 4] becomes [4, 8]

Second iteration
We take the value of 23 and compare it to the values of 4 and 8. This becomes [4, 8, 23]

Third iteration
We take the value of 42 and compare it to the values of 4, 8, and 23. This becomes [4, 8, 23, 42]

Fourth iteration
We take the value of 16 and compare it to the values of 4, 8, 23 and 42. This becomes [4, 8, 16, 23, 42]

Fifth iteration
We take the value of 15 and compare it to the values of 4, 8, 16, 23 and 42. This becomes [4, 8, 15, 16, 23, 42]

This completes our iteration cycle.

