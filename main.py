from binary_tree import BinaryTree

if __name__ == '__main__':
    tree = BinaryTree(5)
    tree.add(3)
    tree.add(4)
    tree.add(2)
    tree.add(6)
    tree.delete(7)
    tree.inorder()
