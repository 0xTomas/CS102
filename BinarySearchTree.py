import random


class BinarySearchTree:
    def __init__(self, value, depth=1):
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None

    def insert(self, value):
        if (value < self.value):
            if (self.left is None):
                self.left = BinarySearchTree(value, self.depth + 1)
                print(f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
            else:
                self.left.insert(value)
        else:
            if (self.right is None):
                self.right = BinarySearchTree(value, self.depth + 1)
                print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
            else:
                self.right.insert(value)

    def get_node_by_value(self, value):
        if (self.value == value):
            return self
        elif ((self.left is not None) and (value < self.value)):
            return self.left.get_node_by_value(value)
        elif ((self.right is not None) and (value >= self.value)):
            return self.right.get_node_by_value(value)
        else:
            return None

    def depth_first_traversal(self):
        if (self.left is not None):
            self.left.depth_first_traversal()
        print(f'Depth={self.depth}, Value={self.value}')
        if (self.right is not None):
            self.right.depth_first_traversal()

    def delete_node_by_value(self, value):
        if (self.value == value):
            print(f'Value: {self.value} deleted at depth {self.depth}')
            self.value = None

        elif (self.left is not None) and (self.left != value):
            return self.left.delete_node_by_value(value)
        elif (self.right is not None) and (self.right != value):
            return self.right.delete_node_by_value(value)
        else:
            print("Value not found.")


print("Creating Binary Search Tree rooted at value 15:")
tree = BinarySearchTree(15)

tree.insert(55)
tree.insert(35)
tree.insert(125)
tree.insert(5)
tree.insert(80)

print("Printing the inorder depth-first traversal:")
tree.depth_first_traversal()

tree.delete_node_by_value(5)
tree.depth_first_traversal()