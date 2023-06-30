from data_structures.stack import Stack

def multi_bracket_validation(str):
    stack = []
    left_brackets = ['[','{','('] #'({['
    right_brackets = [']','}',')'] #')}]'

    for char in str:
        if char in left_brackets:
            stack.append(char)
        elif char in right_brackets:
            if not Stack:
                return False

            top = stack.pop()
            left_brackets = left_brackets.index(top)
            right_brackets = right_brackets.index(char)
            if left_brackets != right_brackets:
            # if (char == ']' and top != '[') or (char == '}' and top != '{') or (char == ')' and top != '('):

                return False
    return len(stack) == 0

# def multi_bracket_validation():
#     pass

# def multi_bracket_validation(str):
#     stack = []
#     left_brackets = ['(','[','{']
#     right_brackets = [')',']','}']


#     for char in str:
#         if char in left_brackets:
#             stack.append(char)
#         elif char in right_brackets:
#             if not stack:
#                 return False


#             top = stack.pop()
#             opening_index = left_brackets.index(top)
#             closing_index = right_brackets.index(char)
#             if opening_index != closing_index:

#                 return False

#     return len(stack) == 0
