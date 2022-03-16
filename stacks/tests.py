import unittest

from stack import Stack


class TestStacks(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = Stack()

    def fill(self, items=1):
        values = ['egg', 'ham', 'spam']
        for i in range(items):
            self.stack.push(values[i])

    def test_push(self):
        self.fill()
        self.assertEqual(self.stack.size, 1)
        self.assertEqual(self.stack.top.data, 'egg')
        self.stack.push('ham')
        self.assertEqual(self.stack.size, 2)
        self.assertEqual(self.stack.top.data, 'ham')

    def test_pop(self):
        self.fill()
        self.assertEqual(self.stack.pop(), 'egg')
        self.assertEqual(self.stack.size, 0)
        self.assertIsNone(self.stack.top)

    def test_peek(self):
        self.fill(2)
        self.assertEqual(self.stack.peek(), 'ham')

    def test_str(self):
        self.assertEqual(self.stack.__str__(), 'Empty stack')
        self.fill()
        self.assertEqual(self.stack.__str__(), 'top egg buttom')

    def test_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.fill()
        self.assertFalse(self.stack.is_empty())

    def test_in(self):
        print('ham' in self.stack)

    def test_clear(self):
        self.fill(3)
        self.stack.clear()
        self.assertIsNone(self.stack.top)

    def test_search(self):
        self.assertEqual(self.stack.search('egg'), 'The stack is empty')
        self.fill(3)
        self.assertEqual(self.stack.search('egg'), 'egg')
        self.assertEqual(self.stack.search('ham'), 'ham')
        self.assertEqual(self.stack.search('spam'), 'spam')
        self.assertIsNone(self.stack.search('hola'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
