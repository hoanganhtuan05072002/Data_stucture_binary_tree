class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class Binary_Tree:
    def __init__(self, root):
        self.root = Node(root)
        
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preoder_print(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(self.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported")
            return False
        
    def preoder_print(self, start, traversal):
        """Root -> Left -> Right"""
        if start:
            traversal += (str(start.data) + "-")
            traversal = self.preoder_print(start.left, traversal)
            traversal = self.preoder_print(start.right, traversal)
        return traversal
    
    def inorder_print(self, start, traversal): 
        """Left -> Root -> Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.data) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.data) + "-")
        return traversal


        # 1-2-4-5-3-6-7-8-
            #          1
            #      /       \
            #     2         3
            #   /  \       /  \
            #  4    5     6    7 
                              # \   
                              #  8
                                 
                
tree = Binary_Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
# tree.root.right.right.right = Node(8)
print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))