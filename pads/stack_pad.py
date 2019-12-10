import unittest
from scratchpad import ScratchpadBase


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
            new_node = StackNode(value, self.head)
            self.head = new_node

    def pop(self):
        if not self.head:
            return

        value = self.head

        if self.head.next:
            self.head = self.head.next
        return value

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

    def populate(self, data_multiplier=1, _params=None):
        if _params:
            self.data_params.update(_params)

        elements = self.data_generator.generate(data_multiplier, self.data_params)
        for element in elements:
            self.push(element)


class StackTests(unittest.TestCase):

    def setUp(self) -> None:
        self.stack = Stack()

    def test_populate(self):
        self.stack.populate(1, {'number_of_nodes': 5})
        self.assertEqual([4,3,2,1,0], self.stack.to_list())

