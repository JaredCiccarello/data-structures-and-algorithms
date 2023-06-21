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

    def insert (self, value):
        self.head = Node(value, self.head)

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
    pass



if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2, node1)
    # [2] -> [1] -> None
    print(node1.value)
    node1.value = 4
    print(node1.value)
