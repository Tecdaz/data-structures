from linked_lists.node import Node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = node

        self.size += 1

    def size(self):
        return self.size

    def __iter__(self):
        current = self.head

        while current is not None:
            val = current.data
            current = current.next
            yield val

    def delete(self, instance):
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
        for node in iter(self):
            if data == node:
                return True

        return False

    def clear(self):
        self.head = None
        self.size = 0

    def __str__(self):
        result = ""
        for node in iter(self):
            result += node+', '
        return result[:len(result)-2]




