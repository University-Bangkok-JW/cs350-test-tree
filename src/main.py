import cls

tree = cls.ArrayTree()

def main():
    
    array = [1, 2, 3, 4, 5, 6, 7]
    tree.arrayToTree(array)

    print("Initial Tree:")
    tree.printArr()
    tree.printInorder()
    tree.printPreorder()
    tree.printPostorder()
    
    print("\nAfter inserting 8:")
    tree.insert(8)
    tree.printArr()
    tree.printInorder()
    
    print("\nAfter inserting multiple values [9, 10]:")
    tree.insertMultiple([9, 10])
    tree.printArr()
    tree.printInorder()
    
    print("\nAfter inserting 11 at index 5:")
    tree.insertAt(5, 11)
    tree.printArr()
    tree.printInorder()

if __name__ == "__main__":
    main()