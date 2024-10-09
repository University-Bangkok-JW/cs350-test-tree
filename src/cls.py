class Tree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class ArrayTree:
    def __init__(self):
        self.root = None
        self.children = []

    def arrayToTree(self, arr):
        if not arr:
            return None

        # Handle incomplete arrays gracefully (suggestion from ratings)
        self.children = [arr[i] if i < len(arr) else None for i in range(len(arr))]
        self.root = self._arrayToTree(0)
        return self.root  # Return the root for convenience

    def _arrayToTree(self, index):
        if index >= len(self.children) or self.children[index] is None:
            return None

        root = Tree(self.children[index])
        root.left = self._arrayToTree(2 * index + 1)
        root.right = self._arrayToTree(2 * index + 2)
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

        # Expand the children list efficiently using extend() (suggestion)
        self.children.extend([None] * (index - len(self.children) + 1))
        self.children[index] = data
        self.root = self._arrayToTree(0)

    """
    Prints the tree elements in inorder traversal (left, root, right).

    Uses a helper function for recursion.
    """

    def printInorder(self):
        def _inorder(node):
            if node:
                _inorder(node.left)
                print(node.data, end=' ')
                _inorder(node.right)

        print('Inorder Traversal:', end=' ')
        _inorder(self.root)
        print()

    """
    Prints the tree elements in preorder traversal (root, left, right).

    Uses a helper function for recursion.
    """
    def printPreorder(self):
        def _preorder(node):
            if node:
                print(node.data, end=' ')
                _preorder(node.left)
                _preorder(node.right)

        print('Preorder Traversal:', end=' ')
        _preorder(self.root)
        print()

    """
    Prints the tree elements in preorder traversal (root, left, right).

    Uses a helper function for recursion.
    """
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