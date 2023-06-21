class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self._next = _next

class LinkedList:
    """
    Put docstring here
    """
    def __init__(self, head=None, values=None, insert=None):
        self.head = None


# LinkedList: Apple.
# Given value: Banana.
    def insert (self, value):
        newNode = Node(value)
        # This is our banana
        newNode._next = self.head
        # This is similar to apple
        self.head = newNode
        # This identifies our next head

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current._next is not None:
                current = current._next
            current._next = newNode

    def insert_before(self, value, new_value):
        current = self.head
        previous = None
        if current is None:
            raise ValueError(f"Value {value} not found in linked list")

        while current is not None and current.value != value:
            previous = current
            current = current._next

        if current is None:
            raise ValueError(f"Value {value} not found in linked list")

        newNode = Node(new_value)
        newNode._next = current
        if previous is None:
            self.head = newNode
        else:
            previous._next = newNode

    def insert_after(self, value, new_value):
        current = self.head
        while current is not None and current.value != value:
            current = current._next

        if current is None:
            raise ValueError(f"Value {value} not found in linked list")

        newNode = Node(new_value)
        newNode._next = current._next
        current._next = newNode



    def __str__(self):
      if self.head == None:
        return "NULL"
      else:
        current = self.head
      output = ""
      while current:
        output += f"{{ {current.value} }} -> "
        current = current._next
      output += "NULL"
      return output

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current._next
        return False

     #kth from end
  #argument: a number, k, as a parameter.
  #Return the node's value that is k places from the tail of the linked list.
  #You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.
    def kth_from_end(self, k):
        current = self.head
        count = 0
        while current:
          count += 1
          current = current._next
        if k < 0 or k >= count:
          raise TargetError("Target not found")
        current = self.head
        for i in range(count - k - 1):
          current = current._next
        return current.value

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current._next


# Putting in exception here fixes the error:
#TypeError: expected exception must be a BaseException type, not TargetError
class TargetError(Exception):



  if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2, node1)
    # [2] -> [1] -> None
    print(node1.value)
    node1.value = 4
    print(node1.value)



# Code Challenge 06
# CD into code_challenges
# Pytest test_linked_list_insertions.py
# pytest-watch-k version_1 < this will watch for any changes to your file
