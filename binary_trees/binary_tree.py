from node import Node


class BinaryTree:
    # El arbol se crea con un valor y lo asigna como raiz
    def __init__(self, data):
        self.root = Node(data)

    # Los valores iguales van siempre a la derecha
    def __add_recursion(self, data, node: Node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.__add_recursion(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.__add_recursion(data, node.right)

    def __preorder_recursion(self, node: Node):
        if node is not None:
            print(node.data)
            self.__preorder_recursion(node.left)
            self.__preorder_recursion(node.right)

    def __inorder_recursion(self, node: Node):
        if node is not None:
            self.__inorder_recursion(node.left)
            print(node.data)
            self.__inorder_recursion(node.right)

    def __postorder_recursion(self, node: Node):
        if node is not None:
            self.__postorder_recursion(node.left)
            self.__postorder_recursion(node.right)
            print(node.data)

    # Retorna el nodo en el que encontro el valor buscado
    def __search_recursion(self, node: Node, target):
        if node is None:
            return None
        elif node.data == target:
            return node
        elif target < node.data:
            return self.__search_recursion(node.left, target)
        else:
            return self.__search_recursion(node.right, target)

    # Busca el hijo mayor por izquierda y redirecciona la direccion del padre
    # para que apunte a los hijos de este y retorna el nodo
    def __mayor_child(self, node: Node, parent: Node):
        if node.right is None:
            parent.right = node.left
            return node
        else:
            return self.__mayor_child(node.right, node)

    def __minor_child(self, node: Node, parent: Node):
        if node.left is None:
            parent.left = node.right
            return node
        else:
            return self.__mayor_child(node.left, node)

    def __replace(self, node):
        if node.left is not None:
            return self.__mayor_child(node.left, node)
        elif node.right is not None:
            return self.__mayor_child(node.right, node)

    def __delete_root(self, target):
        root = self.root
        if root.data == target:
            replace = self.__replace(root)

            if replace is not None:
                replace.left = root.left
                replace.right = root.right

            self.root = replace

    def __delete(self, target, node: Node, parent: Node):
        if node is not None:
            if node.data == target:

                replace = self.__replace(node)

                if replace is not None:
                    replace.left = node.left
                    replace.right = node.right

                if node.data < parent.data:
                    parent.left = replace
                else:
                    parent.right = replace

                del node
            elif target < node.data:
                self.__delete(target, node.left, node)
            else:
                self.__delete(target, node.right, node)

    # Public functions

    def add(self, data):
        self.__add_recursion(data, self.root)

    def preorder(self):
        self.__preorder_recursion(self.root)

    def inorder(self):
        self.__inorder_recursion(self.root)

    def postorder(self):
        self.__postorder_recursion(self.root)

    def search_node(self, target):
        return self.__search_recursion(self.root, target)

    def search(self, target):
        result = self.__search_recursion(self.root, target)
        if result is None:
            return False
        else:
            return True

    def delete(self, target):
        if self.root.data == target:
            self.__delete_root(target)
        else:
            if target < self.root.data:
                self.__delete(target, self.root.left, self.root)
            else:
                self.__delete(target, self.root.right, self.root)
