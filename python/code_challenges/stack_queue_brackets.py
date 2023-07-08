from data_structures.stack import Stack


def multi_bracket_validation(bracket_string):
  #create instance of stack used for storing brackets
  stack = Stack()
  # left_brackets = ['(', '[', '{']
  # right_brackets = [')', ']', '}']

  #create an index of brackets
  bracket_index = {
      #Right, left, right, left, kind of like marching
        ')':'(',
        ']':'[',
        '}':'{'
    }

  for char in bracket_string:
        if char in bracket_index.values():
            stack.push(char)
        elif char in bracket_index.keys():
            if stack.is_empty() or stack.pop() != bracket_index[char]:
                return False

  return stack.is_empty()

# def multi_bracket_validation(bracketString):
    #Setting a variable of stack and then create an instance of the imported class of Stack.

    # stack = Stack()
    # left_brackets = ['[','{','('] #'({['
    # right_brackets = [']','}',')'] #')}]'

    # for char in bracketString:
    #     if char in left_brackets:
    #         stack.push(char)
    #     elif char in right_brackets:
    #         if stack.is_empty:
    #             return False

    #         top = stack.pop()
    #         left_brackets_index = left_brackets.index(top)
    #         right_brackets_index = right_brackets.index(char)
    #         if left_brackets_index != right_brackets_index:
    #             return False

    # return stack.is_empty()
