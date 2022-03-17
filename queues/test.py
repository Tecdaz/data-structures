import unittest

from queues.list_based_queue import ListQueue


class QueuesTest(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = ListQueue()

    def fill(self, items=1):
        values = ['egg', 'ham', 'spam']
        for i in range(items):
            self.queue.enqueue(values[i])

    def test_enqueue(self):
        self.assertEqual(self.queue.__str__(), 'Empty queue')
        self.queue.enqueue('egg')
        self.assertEqual(self.queue.__str__(), "tail ['egg'] head")
        self.assertIn('egg', self.queue)

    def test_dequeue(self):
        self.fill(3)
        for i in range(3):
            self.queue.dequeue()


if __name__ == '__main__':
    unittest.main(verbosity=2)
