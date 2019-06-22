
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

def find_longest_sequence(s):
    
    # Edge cases
    if not s or s[0] == ")" or s[-1] == '(':
        return False

    # create a tuple to hold the two parenthesis
    parenthese_type = ("(", ")")
    # allocate memory for cur_seq_len, longest_seq_len
    cur_seq_len = 0
    longest_seq_len  = 0
    # create a queue
    queue = deque([])

    # loop over string
    for char in s:
        # if queue is currently valid, increment cur_seq_len
        if char == parenthese_type[0]:
            queue.append(char)
            # print('appended curr queue:', queue)
            cur_seq_len += 1
        elif char == parenthese_type[1]:
            try:
                queue.pop()
                cur_seq_len += 1
            except: # if queue is invalid
                # clear cur_seq_len
                cur_seq_len = 0

        # at each iteration, if cur_seq_len is greater than longest_seq_len.
        if cur_seq_len > longest_seq_len:
            # overwrite longest_seq_len val with cur_seq_len
            longest_seq_len = cur_seq_len
    
    return longest_seq_len

        #Pseudocode
            # we go through the string for as long as our is_valid func returns true
            # once it returns false, lets check if its size is larger than our max, override the max.


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

    def test_is_valid_parentheses(self):
        input_1 = is_valid_parentheses('())')
        assert input_1 == False
        input_2 = is_valid_parentheses('((())())')
        assert input_2 == True
        input_3 = is_valid_parentheses('((())')
        assert input_3 == False
        input_4 = is_valid_parentheses('((')
        assert input_4 == False

    def test_find_longest_sequence(self):
        input_1 = find_longest_sequence('())(())')
        assert input_1 == 4

if __name__ == "__main__":
    unittest.main()
