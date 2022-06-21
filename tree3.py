class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class Binary_Search:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                cur_node.left

        else:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)


    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            return True if is_found else False
        else:
            return None
        
    def _find(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        if data == cur_node.data:
            return True
    
    def height(self, node):
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1

bts = Binary_Search(1)
bts.insert(4)
bts.insert(2)
bts.insert(8)
bts.insert(5)
bts.insert(10)
print(bts.find(8))
print(bts.height(bts.root))
            