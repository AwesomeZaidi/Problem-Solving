# Stacks can be relly useful when
#   - you care about the most recent elements
#   - order in which you see and save elements matters.

# Example
# Newfeed page - you need to access the more recent elements more quickly and frequently.

# When you add an element to a stack the operation is called `push`.
# When you take a element off a stack the operation is called `pop`.
# All you need to do is look at the top element for both these operations so the run time
# of these operations should be constant time, O(1).

# Complicated part - because a stack is so abstract it can actually be implemented with another
# data type.  
# What each element looks like and how they're connected aren't actually specified, only the
# methods for adding and removing elements are.
# For example: you can use a Linked List to implement a Stack. You'd keep track of the front
# of a singly linked list and just keep adding elements next as you went.

# L.I.F.O - Last In, First Out!
# All its saying is the last element you push on the stack is the first element you pop from 
# the stack.

# There's a solution below. We had two options here—either pop and push from the first element
# in our linked list, or pop and push from the last element. We already had a function,
# append(), that adds an element to the end.

# Why didn't we just come up with a function for removing the last element and call it a day?
# Every operation on a linked list must start with the head. append() thus traverses the whole
# list, taking O(n). Any operation on the last element requires us to traverse everything,
# so even though we had to write a new method our code will run much faster if we push/pop
# from the first element in a linked list.

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        if self.head:
            deleted_element = self.head
            temp = deleted_element.next
            self.head = temp
            return deleted_element
        else:
            return None

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        return self.ll.delete_first()