class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self._next = _next

class LinkedList:
    """
    Put docstring here
    No I won't do that
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



    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current._next


class TargetError:
    pass


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2, node1)
    # [2] -> [1] -> None
    print(node1.value)
    node1.value = 4
    print(node1.value)
