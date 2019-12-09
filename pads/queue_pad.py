import unittest
from scratchpad import ScratchpadBase


class QueueNode:

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue(ScratchpadBase):

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
        self.tail = None

    def enqueue(self, value):
        if not self.head:
            self.head = QueueNode(value)
            self.tail = self.head
        else:
            self.tail.next = QueueNode(value)
            self.tail = self.tail.next

    def dequeue(self):
        if not self.head:
            return

        value = self.head

        if self.head.next:
            self.head = self.head.next

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
            self.enqueue(element)


class QueueTests(unittest.TestCase):

    def setUp(self) -> None:
        self.queue = Queue()

    def test_populate(self):
        self.queue.populate(1, {'number_of_nodes': 5})
        self.assertEqual([0,1,2,3,4], self.queue.to_list())

