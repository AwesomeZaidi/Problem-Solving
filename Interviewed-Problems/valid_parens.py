
'''
# Given a string containing open and closed parenthesis, write a function to determine if the given sequence is valid or not.
# Given a string containing open and closed parethensis, write a function to determine the length of the longest valid sequence from the input. 

# (((())))))(((())))((()))))): 

# ()( :yes
# (()) :yes  (())((( : 4  --  (())((()))
# ()() :yes
# ()   :yes
# )(   :no  
# (()  :no
# ())  :no
  
# ())(() : no

Question : Given a string input of parentheses, retur true or false if they are valid.
Examples: "(())" -> True , "())" -> False , "()()()" -> True
Time : 15 minutes
Difficulty : Easy-Medium
'''


from collections import deque
import unittest

def is_valid_parentheses(s):
    if not s or s[0] == ")" or s[-1] == '(':
        return False
    parenthese_type = ("(", ")")

    queue = deque([]) 

    for char in s:
        if char == parenthese_type[0]:
            queue.append(char)
        elif char == parenthese_type[1]:
            try:
                queue.popleft()
            except:
                return False

    if len(queue) == 0:
        return True

    return False


class ValidParens(unittest.TestCase):

    def test(self):
        input_1 = is_valid_parentheses('())')
        assert input_1 == False
        input_2 = is_valid_parentheses('((())())')
        assert input_2 == True
        input_3 = is_valid_parentheses('((())')
        assert input_3 == False
        input_4 = is_valid_parentheses('((')
        assert input_4 == False

if __name__ == "__main__":
    unittest.main()
