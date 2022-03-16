from linked_lists.node import Node


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __str__(self):
        if self.top is None:
            return 'Empty stack'
        else:
            result = 'top '
            pointer = self.top
            while pointer:
                result += str(pointer.data) + ' '
                pointer = pointer.next
            result += 'buttom'
            return result

    def __iter__(self):
        pointer = self.top
        while pointer:
            val = pointer.data
            pointer = pointer.next
            yield val

    def __len__(self):
        return self.size

    def search(self, target):
        """Busca un elemento y si lo encuentra retorna el elemento, sino retorna None"""
        if self.is_empty():
            return "The stack is empty"
        #Con ayuda del iterador, este recorre la pila y retorna True o False dependiendo si existe o no el elemento buscado
        elif target in self:
            return target
        else:
            return None

    def is_empty(self):
        """Retorna un valor booleano, si la lista esta vacia"""
        return self.top is None

    def push(self, data):
        """Ingresa un nuevo valor y lo pone en el tope"""
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

        self.size += 1

    def pop(self):
        """Elimina el valor del tope y retorna su valor"""
        if self.top:
            data = self.top.data
            self.size -= 1

            self.top = self.top.next

            return data

        else:
            return "The stack is empty"

    def peek(self):
        """Retorna el valor del tope de la pila"""
        if self.top:
            return self.top.data
        else:
            return 'The stack is empty'

    def clear(self):
        """Vacia la pila"""
        while self.top:
            self.pop()
