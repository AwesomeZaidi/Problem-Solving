# Remove Nth Node From End of List

# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:

# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def removeNthFromEnd(self, head, n):
#         def index(node):
#             if not node:
#                 return 0
#             i = index(node.next) + 1
#             if i > n:
#                 node.next.val = node.val
#             return i
#         index(head)
#         return head.next

def delete_node(self, key):
    cur_node = self.head

    if  cur_node and cur_node.data == key:
        self.head = cur_node.next
        cur_node = None
        return

    prev_node = None 
    while (cur_node and cur_node.data != key):
        prev_node = cur_node
        cur_node = cur_node.next

    if cur_node == None:
        return
    
    # element is present
    prev_node.next = cur_node.next
    cur_node.next = None

def delete_node_at_pos(pos):

    cur_node = self.head

    if pos == 0:
        self.head = cur_node.next
        cur_node = None
        return
    
    prev = None
    count = 1
    while cur_node and count != pos:
        prev = cur_node
        cur_node = cur_node.next
        count += 1
    
    if cur_node == None:
        return
    
    # element is present
    prev_node.next = cur_node.next
    cur_node.next = None