import unittest
from AlgorithmScratchpad.scratchpad import ScratchpadBase


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

        node = self.head

        self.head = node.next
        if not self.head:
            self.tail = None

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
            self.enqueue(element)


class QueueTests(unittest.TestCase):

    def setUp(self) -> None:
        self.queue = Queue({
            'type': 'list',
            'fill_with': 'unsigned',
            'sort': 'asc',
            'number_of_nodes': 5,
            'test_run': {
                'number_of_nodes': 10
            }
        })


    def test_populate_control(self):
        self.queue.populate('control')
        self.assertEqual([0,1,2,3,4], self.queue.to_list())

    def test_populate_test(self):
        self.queue.populate('test')
        self.assertEqual([0,1,2,3,4,5,6,7,8,9], self.queue.to_list())

    def test_dequeue(self):
        self.queue.populate('control')
        self.queue.dequeue()
        self.queue.dequeue()
        self.queue.dequeue()
        self.assertEqual(3, self.queue.dequeue())

    def test_over_dequeue(self):
        self.queue.dequeue()
        self.queue.dequeue()
        self.queue.dequeue()
        self.queue.dequeue()
        self.queue.dequeue()
        self.assertEqual(None, self.queue.dequeue())

