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

    def __len__(self):
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

    def __index_error(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('Accedio a un indice fuera de la lista')

    def __getitem__(self, item):
        self.__index_error(item)
        count = 0
        current = self.head
        while current is not None:
            if count == item:
                return current.data
            count += 1
            current = current.next

    def __setitem__(self, key, value):
        self.__index_error(key)
        if key == 0:
            self.head.data = value
        else:
            counter = 1
            current = self.head.next

            while counter < key:
                current = current.next
                counter += 1
            current.data = value

    def __str__(self):
        result = ""
        for node in iter(self):
            result += str(node) + ', '
        # Retorna el string con el resultado y le resta los ultimos dos espacios
        return result[:len(result) - 2]

    def insert_start(self, data):
        """Inserta un nodo al principio de la lista"""
        new_node = Node(data, self.head)
        self.head = new_node
        self.size += 1

    def insert_position(self, index, data):
        """Inserta un nodo en la posicion dada"""
        self.__index_error(index)
        if index == 0:
            self.insert_start(data)
        else:
            current = self.head
            while index > 1:
                index -= 1
                current = current.next
            new_node = Node(data, current.next)
            current.next = new_node
            self.size += 1

    def del_index(self, index):
        """Elimina un nodo en el indice indicado"""
        self.__index_error(index)
        if index == 0:
            self.head = self.head.next
            self.size -= 1
        else:
            counter = 1
            current = self.head
            while counter < index:
                counter += 1
                current = current.next
            current.next = current.next.next
            self.size -= 1

    def del_end(self):
        """Elimina el final de la lista"""
        if self.head is None:
            raise Exception('Empty list')

        elif self.head.next is None:
            self.head = None
            self.size -= 1
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None
            self.size -= 1
