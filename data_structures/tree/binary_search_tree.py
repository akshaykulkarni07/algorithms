class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        pass
    
    def insert_(self, start, new_val):
        if start.value < new_val:
            if start.right:
                self.insert_(start.right, new_val)
            else:
                start.right = Node(new_val)
        else:
            if start.left:
                self.insert_(start.left, new_val)
            else:
                start.left = Node(new_val)

    def search(self, find_val):
        return self.search_(self.root, find_val)
    
    def search_(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            elif start.value < find_val:
                return self.search_(start.right, find_val)
            else:
                return self.search_(start.left, find_val)
        return False

if __name__ == '__main__':
    # Set up tree
    tree = BST(4)

    # Insert elements
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)

    # Check search
    # Should be True
    print(tree.search(4))
    # Should be False
    print(tree.search(6))