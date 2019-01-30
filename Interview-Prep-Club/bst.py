# A utility class that represents an individual node in a BST 
class Node:
    def __init__(self, key): 
        self.left_child = None # left leef
        self.right_child = None # right leef
        self.val = key
    
    # def get(self):
    #     return self.val
    
    # def set(self, val):
    #     self.val = val
    
    # def get_children(self):
    #     # create empty array of children
    #     children = []
    #     # if we have a left child, append it.
    #     if (self.left_child != None):
    #         children.append(self.left_child)
    #     # if we have a right child, append it.
    #     if (self.right_child != None):
    #         children.append(self.right_child)
        
    #     return children

    def __str__(self):
        return str(self.val) #return as string
        
class BST:
    """
        Binary Search Tree Class
    """
    def __init__(self): # constructor of class
        self.root = None
    
    def set_root(self, val):
        self.root = Node(val)
    
    def insert(self, val):
        
        if (self.root is None): # for the first element
            self.set_root(val)
        else:
            self.insert_node(self.root, val)

    def insert_node(self, current_node, val):
        """
            Args:
                current_node : self.root
                val         : val (that you pass in)
        """
        # if the val is less than the current val
        if (val <= current_node.val):
            # check if it has a val to the left
            if (current_node.left_child):
                # if so, recursion, run the function again with the new node!
                self.insert_node(current_node.left_child, val)
            else:
                # else, set the left child with the new Node val!
                current_node.left_child = Node(val)
        elif (val > current_node.val):
            # check if it has a val to the right
            if (current_node.right_child):
                # if so, recursion, run the function again with the new node!
                self.insert_node(current_node.right_child, val)
            else:
                # else, set the right child with the new Node val!
                current_node.right_child = Node(val)

    def find(self, val):
        return self.find_node(self.root, val)

    def find_node(self, current_node, val):
        """
            Args:
                current_node: self.root
                val: val
            Returns:
                - False is the Node is nonexistant.
                - True if we find the Node
        """
        if (current_node is None):
            return False
        elif (val == current_node.val):
            return True
        elif (val < current_node.val):
            return self.find_node(current_node.left_child, val)
        else:
            return self.find_node(current_node.right_child, val)



# OTHER CODE
#  A utility function to search a given key in BST 
# def search(root, node): 
    
#     # Base Cases: root is null or key is present at root 
#     if root is None or root.val == key: 
#         return root

#     # Key is greater than root's key 
#     if root.val < key: 
#         return search(root.right,key) 
    
#     # Key is smaller than root's key 
#     return search(root.left,key)

# This code is contributed by Bhavya Jain 