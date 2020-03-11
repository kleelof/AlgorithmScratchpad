import unittest
from AlgorithmScratchpad.scratchpad import ScratchpadBase


class StackNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = None if not next else next


class Stack(ScratchpadBase):
    def __init__(self, _data_params=None):

        data_params = {
            'type': 'list',
            'fill_with': 'unsigned',
            'sort': 'asc'
        }
        if _data_params:
            data_params.update(_data_params)

        super().__init__(data_params)

        self.head = None

    def push(self, value):
        if not self.head:
            self.head = StackNode(value)
        else:
            self.head = StackNode(value, self.head)

    def pop(self):
        if not self.head:
            return

        node = self.head
        self.head = self.head.next

        return node.value

    def print_me(self):
        if self.head:
            node = self.head
            print(f'{node.value}')
            while node.next:
                print(f'{node.next.value}')
                node = node.next

    def to_list(self):
        _list = []
        if self.head:
            node = self.head
            _list = [node.value]
            while node.next:
                _list.append((node.next.value))
                node = node.next
        return _list

    def populate(self, run, _params=None):
        if _params:
            self.data_params.update(_params)

        elements = self.data_generator.generate(run, self.data_params)
        for element in elements:
            self.push(element)


class StackTests(unittest.TestCase):

    def setUp(self) -> None:
        self.stack = Stack({
            'type': 'list',
            'fill_with': 'unsigned',
            'sort': 'asc',
            'number_of_nodes': 5,
            'test_run': {
                'number_of_nodes': 10
            }
        })

    def test_populate_control(self):
        self.stack.populate('control')
        self.assertEqual(5, len(self.stack.to_list()))

    def test_populate_test(self):
        self.stack.populate('test')
        self.assertEqual(10, len(self.stack.to_list()))

    def test_push_pop(self):
        self.stack.push('a')
        self.stack.push('b')
        self.assertEqual('b', self.stack.pop())
        self.assertEqual('a', self.stack.pop())


