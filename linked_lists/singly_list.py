from linked_lists.node import Node


class SinglyLinkedList:
    def __init__(self):
        """La lista se inicia apuntando a None"""
        self.head = None
        self.size = 0

    def append(self, data):
        """Agrega un nuevo nodo al final de la lista"""
        node = Node(data)
        # Para el primer elemento de la lista, sino un puntero recorre hasta llegar al final de la misma
        if self.head is None:
            self.head = node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = node

        self.size += 1

    def size(self):
        """Tamaño de la lista"""
        return self.size

    def __iter__(self):
        current = self.head

        while current is not None:
            val = current.data
            current = current.next
            yield val

    def delete(self, instance):
        """Elimina un valor de la lista y lo retorna, si el valor no existe no retorna ni hace nada"""
        current = self.head
        previous = self.head

        while current is not None:
            if current.data == instance:
                if current == self.head:
                    self.head = current.next
                else:
                    previous.next = current.next
                self.size -= 1
                return current.data

            previous = current
            current = current.next

    def search(self, data):
        """Busca un elemento en la lista y retorna un valor booleano"""
        for node in iter(self):
            if data == node:
                return True

        return False

    def clear(self):
        """Borra toda la lista"""
        self.head = None
        self.size = 0

    def __str__(self):
        result = ""
        for node in iter(self):
            result += str(node) + ', '
        # Retorna el string con el resultado y le resta los ultimos dos espacios
        return result[:len(result) - 2]
