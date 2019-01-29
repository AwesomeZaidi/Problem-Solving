class BinarySearchTree:
    
    __init__(self):
            self.root = None
            self.size = 0


    def length(self):
        return self.size

    def __len__(self):
        return self.size
    
    # def __iter__(self):
    #     return self.root.__iter__()

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

 