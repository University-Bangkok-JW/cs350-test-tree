class Tree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class ArrayTree:
    def __init__(self, arr):
        self.root = None
        self.children = []

    def arrayToTree(self, arr):
        if not arr:
            return None
        self.data = arr
        self.root = self._arrayToTree(0)

    def _arrayToTree(self, index):
        if index < len(self.children) or self.children[index] is None:
            return None
        
        root = Tree(self.children[index])
        # Left child = 2*i + 1
        root.left = self._arrayToTree(2*index + 1)
        # Right child = 2*i + 2
        root.right = self._arrayToTree(2*index + 2)

        return root

    def insert(self, data):
        self.children.append(data)
        self.root = self._arrayToTree(0)

    def insertMultiple(self, arr):
        for data in arr:
            self.insert(data)

    def insertAt(self, index, data):
        if index < 0:
            return
        
        while len(self.children) <= index:
            self.children.append(None)
    
    def printInorder(self):
        def _inorder(node):
            if node:
                _inorder(node.left)
                print(node.data, end=' ')
                _inorder(node.right)

            print('Inorder Traversal:', end=' ')
            _inorder(self.root)
            print()

    def printPreorder(self):
        def _preorder(node):
            if node:
                print(node.data, end=' ')
                _preorder(node.left)
                _preorder(node.right)

            print('Preorder Traversal:', end=' ')
            _preorder(self.root)
            print()

    def printPostorder(self):
        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                print(node.data, end=' ')

            print('Postorder Traversal:', end=' ')
            _postorder(self.root)
            print()

    def printArr(self):
        print('Array Representation:', self.children)
