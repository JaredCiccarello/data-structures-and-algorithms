
Collaborators
Anthony Sinitsa
Daniel Quinn
Andrew Carroll

# Challenge Title
Code Challenge: Class 03

## Whiteboard Process
Image
![CodeChallenge06](<Screenshot 2023-06-20 180811.png>)
## Approach & Efficiency

## Solution
Starting with the insert, you set value to head.
Set next newNode to next and equal self.head, this tells the value to move.
self.head = newNode which moves your new value into node1, telling your value where to move.
Next we need to create an append function. marking self.head to None. This allows for us to set a new value to our newNode variable.
We identify what our current is in our Node, which is self.head in this case.
We create a while loop to iterate over our node values until we arrive at the desired result.
current._next is not None: sets our condition in our while loop. Whatever the current head value is, we move the value and
 then define our newNode
We create a function to set the before and after for our inserts in order to set parameters
