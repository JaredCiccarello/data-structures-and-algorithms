from data_structures.stack import Stack


class PseudoQueue:
    def __init__(self):
      # These are two stack instances
      self.enqueue_stack = Stack()
      self.dequeue_stack = Stack()

    def enqueue(self, value):
            #We want to push values to the end of the queue
            self.dequeue_stack.push(value)

    def dequeue (self):
          #We need to check if the queue is empty
          #If it is raise exception
          if self.is_empty():
            return Exception("Cannot dequeu from empty queue")

          #Move elements from enqueue stack to dequeue stack
          if self.enqueue_stack.is_empty():
           while not self.dequeue_stack.is_empty():
              self.enqueue_stack.push(self.dequeue_stack.pop())

          #Return value from the front of the queue
          return self.enqueue_stack.pop()


    def is_empty(self):
            return self.enqueue_stack.is_empty() and self.dequeue_stack.is_empty()


# Need to have a way to move enqueue_stack back to dequeue_stack





    # def enqueue(self, value):
    #   #We need a way to traverse over our stack, a while loop
    #   #is_empty is a method
    #   while not self.dequeue_stack.is_empty():
    #     #In order to move values from dequeue stack to enqueue stack we use the pop method.
    #     #Before we determine if the dequeue stack is empty or not then we
    #     self.enqueue_stack.push(value)

    # def dequeue(self):
    #     if self.is_empty():
    #         raise IndexError("Cannot dequeue from an empty pseudo queue")

    #     while not self.enqueue_stack.is_empty():
    #         self.dequeue_stack.push(self.enqueue_stack.pop())

    #     return self.dequeue_stack.pop()

    # def is_empty(self):
    #     return self.enqueue_stack.is_empty() and self.dequeue_stack.is_empty()
