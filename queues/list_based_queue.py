class ListQueue:
    def __init__(self):
        self.items = []
        self.size = 0

    def __str__(self):
        if self.size > 0:
            result = 'tail '
            result += str(self.items)
            result += ' head'
            return result
        else:
            return 'Empty queue'

    def __len__(self):
        return len(self.items)

    def enqueue(self, data):
        self.items.insert(0, data)
        self.size += 1

    def dequeue(self):
        data = self.items.pop()
        self.size -= 1
        return data

    def __iter__(self):
        for i in range(len(self.items)):
            yield self.items[i]

    def __getitem__(self, item):
        return self.items[item]
